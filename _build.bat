@echo off
REM build pyd
py setup.py build_ext --inplace
echo.
REM build wheel
py setup.py bdist_wheel --py-limited-api=cp36
pause