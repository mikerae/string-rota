# Test Fixes Action Plan

**Date:** 22 January 2026  
**Status:** Ready to implement  
**Priority:** 🔴 HIGH

---

## 📌 Executive Summary

**Problem:** 2 tests failing due to missing `crispy-bootstrap4` package  
**Solution:** Install package and update Django settings  
**Impact:** Will fix 2 failing tests, achieving 100% (66/66) test pass rate  
**Effort:** ~5-10 minutes

---

## 🎯 Fix 1: Install crispy-bootstrap4

### What to Do
Install the missing Python package that provides Bootstrap4 templates for Crispy Forms.

### Command
```bash
pip install crispy-bootstrap4
```

### Why This Works
- Crispy Forms renders forms using template packs
- Tests render views with forms using Bootstrap4 styling
- Bootstrap4 template pack is not installed (missing 1,600+ template files)
- Installing package adds the `bootstrap4/uni_form.html` template being sought

### Expected Output
```
Successfully installed crispy-bootstrap4-x.x.x
```

### Verification
```bash
pip list | grep crispy
```

---

## 🎯 Fix 2: Update Django Settings

### What to Do
Add `crispy_bootstrap4` to INSTALLED_APPS in Django settings.

### File
[django_string_rota/settings.py](../django_string_rota/settings.py)

### Change Required
Find this section:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # ... more apps ...
    'crispy_forms',
    # ... more apps ...
]
```

Add after `'crispy_forms'`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # ... more apps ...
    'crispy_forms',
    'crispy_bootstrap4',  # ← ADD THIS LINE
    # ... more apps ...
]
```

### Why This Works
- Django needs to know which template pack crispy forms should use
- Adding app to INSTALLED_APPS registers the bootstrap4 templates
- Allows Django to find and serve the templates when tests render views

### Optional Enhancement
After INSTALLED_APPS, add explicit configuration (already done but verify):
```python
CRISPY_TEMPLATE_PACK = "bootstrap4"
```

---

## 📋 Implementation Checklist

### Step 1: Install Package
- [ ] Run: `pip install crispy-bootstrap4`
- [ ] Verify: `pip list | grep crispy-bootstrap4`

### Step 2: Update Settings
- [ ] Open [django_string_rota/settings.py](../django_string_rota/settings.py)
- [ ] Locate INSTALLED_APPS list
- [ ] Add `'crispy_bootstrap4',` after `'crispy_forms',`
- [ ] Save file

### Step 3: Verify Installation
- [ ] Run: `python manage.py check`
- [ ] Should output: `System check identified no issues (0 silenced).`

### Step 4: Run Tests
- [ ] Run: `python manage.py test string_rota -v 2`
- [ ] Should see: `Ran 66 tests ... OK`

### Step 5: Commit Changes
- [ ] Stage: `git add django_string_rota/settings.py`
- [ ] Commit: `git commit -m "Add crispy_bootstrap4 to INSTALLED_APPS for Bootstrap4 form rendering"`

### Step 6: Update Dependencies (if applicable)
- [ ] If using pyproject.toml: Add `crispy-bootstrap4` to dependencies
- [ ] If using requirements.txt: Add `crispy-bootstrap4` to file
- [ ] If using poetry.lock: Run `poetry add crispy-bootstrap4`

---

## 🔍 Test Expectations After Fixes

### Current State (Before Fixes)
```
Ran 66 tests in 22.731s
FAILED (errors=2)

ERROR: test_add_seating_position_view_get
ERROR: test_reserve_view_get
```

### Expected State (After Fixes)
```
Ran 66 tests in ~22s
OK

All tests pass ✅
```

---

## 🚨 Troubleshooting

### Issue: Installation fails
**Error:** `ERROR: Could not find a version that satisfies the requirement crispy-bootstrap4`
**Solution:** 
- Verify Python version: `python --version`
- Try: `pip install --upgrade pip`
- Try: `pip install crispy-bootstrap4 --no-cache-dir`

### Issue: After install, tests still fail
**Error:** Still see `TemplateDoesNotExist: bootstrap4/uni_form.html`
**Solution:**
- Verify INSTALLED_APPS updated: `grep -n crispy_bootstrap4 django_string_rota/settings.py`
- Restart Django development server (if any running)
- Verify file saved: `cat django_string_rota/settings.py | grep -A 5 crispy`

### Issue: `Module not found: crispy_bootstrap4`
**Error:** `ModuleNotFoundError: No module named 'crispy_bootstrap4'`
**Solution:**
- Check if in virtual environment: `which python`
- Ensure pip is for same environment: `which pip`
- Try: `python -m pip install crispy-bootstrap4`

---

## 📝 Files to Modify

| File | Action | Changes |
|------|--------|---------|
| django_string_rota/settings.py | Modify | Add `'crispy_bootstrap4',` to INSTALLED_APPS |
| pyproject.toml or requirements.txt | Modify | Add `crispy-bootstrap4` to dependencies |
| (none in code) | N/A | No test code changes needed |

---

## ✅ Success Criteria

After implementing fixes, verify:
1. [ ] Installation command runs without errors
2. [ ] Settings file contains `'crispy_bootstrap4'` in INSTALLED_APPS
3. [ ] `python manage.py check` reports no issues
4. [ ] `python manage.py test string_rota` shows 66/66 passing
5. [ ] No `TemplateDoesNotExist` errors in output

---

## 🎓 Why This Solution Works

### Root Cause Analysis
- **Problem:** Tests render HTML with Crispy Forms
- **Crispy Forms:** Uses template packs to style forms
- **Current Setting:** `CRISPY_TEMPLATE_PACK = "bootstrap4"`
- **Missing:** Bootstrap4 template pack files (requires separate package)
- **Solution:** Install `crispy-bootstrap4` which provides the template files

### The Fix
1. Install provides 1,600+ template files for Bootstrap4 styling
2. Add to INSTALLED_APPS so Django loads them
3. Tests now find `bootstrap4/uni_form.html` when rendering
4. Template renders successfully, tests pass

---

**Ready to proceed? Confirm and start fixes.**
