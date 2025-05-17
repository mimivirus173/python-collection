@echo off
:start
cls
title Available options
echo Pygame: basic, smooth movement test 
echo Other games: guessnum, rng
echo Miscellaneous: cleartest, keypressnum, keyreg, percentage bar
echo Calculators: ammonia temp scale, hardy-weinberg, ohms lambda, ohms law, quadratic equation, stigmet
echo Other tools: passgen
echo:
set /p choice=Choose: 
cls

if "%choice%"=="basic" goto basic
if "%choice%"=="smooth movement test" goto smooth_movement_test
if "%choice%"=="guessnum" goto guessnum
if "%choice%"=="rng" goto rng
if "%choice%"=="cleartest" goto cleartest
if "%choice%"=="keypressnum" goto keypressnum
if "%choice%"=="keyreg" goto keyreg
if "%choice%"=="percentage bar" goto percentage_bar
if "%choice%"=="hardy-weinberg" goto hardy_weinberg
if "%choice%"=="ohms lambda" goto ohms_lambda
if "%choice%"=="ohms law" goto ohms_law
if "%choice%"=="quadratic equation" goto quadratic_equation
if "%choice%"=="ammonia temp scale" goto ammonia_temp_scale
if "%choice%"=="passgen" goto passgen
if "%choice%"=="stigmet" goto stigmet

echo Invalid choice! Try again.
pause
goto start

:basic
title basic.py
python "games/pygame/basic.py"
goto end

:smooth_movement_test
title smooth movement test.py
python "games/pygame/smooth movement test.py"
goto end

:guessnum
title guessnum.py
python "games/guessnum.py"
goto end

:rng
title rng.py
python "games/rng.py"
goto end

:cleartest
title cleartest.py
python "misc/cleartest.py"
goto end

:keypressnum
title keypressnum.py
python "misc/keypressnum.py"
goto end

:keyreg
title keyreg.py
python "misc/keyreg.py"
goto end

:percentage_bar
title percentage bar.py
python "misc/percentage bar.py"
goto end

:hardy_weinberg
title hardy-weinberg.py
python "tools/calc/hardy-weinberg.py"
goto end

:ohms_lambda
title ohms law.py
python "tools/calc/ohms lambda.py"
goto end

:ohms_law
title ohms law.py
python "tools/calc/ohms law.py"
goto end

:quadratic_equation
title quadratic equation.py
python "tools/calc/quadratic equation.py"
goto end

:ammonia_temp_scale
title ammonia temp scale.py
python "tools/calc/ammonia temp scale.py"
goto end

:passgen
title passgen.py
python "tools/passgen.py"
goto end

:stigmet
title stigmet.py
python "tools/calc/stigmet.py"
goto end

:end
pause