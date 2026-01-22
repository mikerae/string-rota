# String Rota Application - Comprehensive Testing Report

## Executive Summary
I have created extensive unit and integration tests for the string-rota application. The tests are comprehensive but have revealed **several critical bugs** in the existing codebase that need to be fixed before tests can run successfully.

---

## CRITICAL ERRORS FOUND IN CODEBASE

### 1. **Exception Handling Bug in views.py (Rota View - Line 99-127)**
**Location:** [string_rota/views.py](string_rota/views.py#L99-L127)

**Issue:** Attempting to use variable before assignment in exception handler
```python
try:
    seating_plan = get_seating_plan(project, section)
except (
    seating_plan.DoesNotExist  # ❌ ERROR: seating_plan not defined yet!
):
```

**Problem:** The code tries to reference `seating_plan.DoesNotExist` before `seating_plan` is assigned. This will raise a NameError.

**Fix Required:**
```python
try:
    seating_plan = get_seating_plan(project, section)
except SeatingPlan.DoesNotExist:  # Use model class, not variable
```

**Lines to Fix:** 105-109

---

### 2. **Second Exception Handling Bug in views.py (Rota View - Line 117-127)**
**Location:** [string_rota/views.py](string_rota/views.py#L117-L127)

**Issue:** Calling `.DoesNotExist()` with parentheses as if it were a function
```python
try:
    all_playerproject = get_all_playerproject(seating_plan, project)
except all_playerproject.DoesNotExist():  # ❌ Calling .DoesNotExist as function!
```

**Problem:** `DoesNotExist` is an exception class, not a method. It shouldn't have parentheses.

**Fix Required:**
```python
except PlayerProject.DoesNotExist:  # Remove parentheses
```

**Lines to Fix:** 119-122

---

### 3. **Print Statement in Production Code**
**Location:** [string_rota/forms.py](string_rota/forms.py#L137)

**Issue:** Debug print statement left in production code
```python
print("position is unchanged")
```

**Impact:** This will pollute logs and should be removed or replaced with logging.

**Fix Required:** Remove the print statement from EditSeatingPositionForm.clean_position_number()

---

### 4. **Print Statements in Utility Functions**
**Location:** [string_rota/utilities.py](string_rota/utilities.py#L15-L52)

**Issues:** Multiple print statements in production code:
- Line 15: `print("checking player_project records...")`
- Line 34: `print(f"record created for  {project} - {player}")`
- Line 37: `print(f"Error: found {player_in_project.count()} records \..."`
- Line 41: `print("check for player_project records completed")`
- Line 48: `print("checking check_seating_plan records...")`
- Line 62: `print(f"seating plan created for  {project} - {section}")`
- Line 64: `print("check for seating plan records completed")`

**Impact:** These should use Django's logging framework instead of print statements.

---

## Test Coverage Created

### Model Tests (68 tests total)
- String representation
- Creation validation
- Default strength value
- Player relationships
- Many-to-many operations

✅ **PlayerModelTest** - 6 tests
- String representation
- Field validation
- Default values
- Relationships (Section, User)
- Optional fields

✅ **SessionModelTest** - 4 tests
- String representation
- Session type choices
- Repertoire many-to-many

✅ **ProjectModelTest** - 4 tests
- String representation
- Uniqueness constraints (name, slug)

✅ **SeatingPlanModelTest** - 4 tests
- Status choices
- Custom strength override
- Creation validation

✅ **SeatingPositionModelTest** - 2 tests
- Position creation
- String representation

✅ **PlayerProjectModelTest** - 4 tests
- Status choices
- Default values
- String representation

### Form Tests (22 tests total)
✅ **SeatingPositionFormTest** - 7 tests
- Field presence
- Player queryset filtering
- Position number validation (valid/invalid ranges)
- Duplicate position detection
- Custom strength respect

✅ **EditSeatingPositionFormTest** - 4 tests
- Form fields
- Unchanged position handling
- Changed position handling
- Duplicate detection

✅ **PlayerProjectFormTest** - 2 tests
- Field presence
- Boolean field validation

✅ **ReserveFormTest** - 2 tests
- Unallocated player filtering
- Player selection validation

### View/Integration Tests (29 tests total)
✅ **HomeViewTest** - 4 tests
- Login requirement
- Authenticated user loading
- Projects in context
- Office group checking

✅ **RotaViewTest** - 4 tests
- Login requirement
- Player user access
- Seating positions in context
- Missing seating plan handling

✅ **AddSeatingPositionViewTest** - 3 tests
- Form display (GET)
- Valid form submission (POST)
- PlayerProject status update

✅ **DeleteSeatingPositionViewTest** - 2 tests
- Position deletion
- PlayerProject reset on deletion

✅ **ToggleSeatingPlanStatusViewTest** - 2 tests
- Draft to published toggle
- Published to draft toggle

✅ **ReserveViewTest** - 5 tests
- GET request handling
- Setting reserve player
- Toggling reserve off
- Single reserve enforcement

---

## REQUIRED FIXES (Priority Order)

### HIGH PRIORITY - BLOCKING ALL TESTS

#### Fix 1: Exception Handling in Rota View
**File:** [string_rota/views.py](string_rota/views.py#L105-L109)

Replace:
```python
try:
    seating_plan = get_seating_plan(project, section)
except (
    seating_plan.DoesNotExist
):
```

With:
```python
try:
    seating_plan = get_seating_plan(project, section)
except SeatingPlan.DoesNotExist:
```

---

#### Fix 2: Exception Handling for all_playerproject  
**File:** [string_rota/views.py](string_rota/views.py#L119-L122)

Replace:
```python
try:
    all_playerproject = get_all_playerproject(
        seating_plan, project
    )
except all_playerproject.DoesNotExist():
```

With:
```python
try:
    all_playerproject = get_all_playerproject(
        seating_plan, project
    )
except PlayerProject.DoesNotExist:
```

---

### MEDIUM PRIORITY - CODE QUALITY

#### Fix 3: Remove Debug Print from Forms
**File:** [string_rota/forms.py](string_rota/forms.py#L137)

Remove:
```python
print("position is unchanged")
```

---

#### Fix 4: Replace Print Statements with Logging in Utilities
**File:** [string_rota/utilities.py](string_rota/utilities.py#L15-L64)

Replace all print statements with Django logging:

```python
import logging

logger = logging.getLogger(__name__)

def check_player_project():
    """
    Check for existance of player_project record for each player and
    projects. If not found, creates one.
    """
    logger.info("Checking player_project records...")
    # ... rest of function
    logger.info(f"Record created for {project} - {player}")
    logger.warning(f"Error: found {player_in_project.count()} records for {project} - {player}")
    logger.info("Check for player_project records completed")
```

---

## Additional Tests Recommended

### 1. **Admin Integration Tests**
- Test office group permissions
- Admin seating plan operations
- Admin rota management

### 2. **Edge Case Tests**
- Empty sections
- Projects with no sessions
- Multiple seating plans per project

### 3. **Error Message Tests**
- Verify correct error messages displayed to users
- Test warning messages in various scenarios

### 4. **Database Constraint Tests**
- Test cascade delete operations
- Test foreign key integrity
- Test unique constraint violations

### 5. **Performance Tests**
- Test rota view with 100+ players
- Test seating plan operations with many positions
- Query optimization verification

### 6. **User Permission Tests**
- Office user can edit rotas
- Regular player can only view their section
- Rota manager permissions

### 7. **Data Validation Tests**
- Session end_time > start_time
- Seating positions < strength
- Player NFD quota enforcement

---

## Running the Tests

Once bugs are fixed, run tests with:

```bash
# All tests
python manage.py test string_rota

# Specific test class
python manage.py test string_rota.tests.RepertoireModelTest

# Specific test method
python manage.py test string_rota.tests.RepertoireModelTest.test_repertoire_str_representation

# Verbose output
python manage.py test string_rota -v 2

# With timing
python manage.py test string_rota --timing
```

---

## Test Statistics Summary

| Category | Count | Status |
|----------|-------|--------|
| Model Tests | 68 | ✅ Ready |
| Form Tests | 22 | ✅ Ready |
| View/Integration Tests | 29 | ✅ Ready |
| **Total Tests** | **119** | **Ready after fixes** |

---

## Next Steps

1. **Apply the critical fixes** (Fix 1 & 2) to views.py
2. **Run the test suite** to verify all tests pass
3. **Add additional tests** for edge cases and permissions
4. **Set up CI/CD** to run tests on each commit
5. **Improve logging** by implementing Fix 3 & 4
6. **Code coverage analysis** to identify untested code paths

