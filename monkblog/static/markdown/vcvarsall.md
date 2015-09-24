http://stackoverflow.com/questions/19830942/pip-install-gives-error-unable-to-find-vcvarsall-bat

$ pip install Flask-Misaka
Collecting Flask-Misaka
  Downloading Flask-Misaka-0.3.0.tar.gz (168kB)
    100% |################################| 172kB 694kB/s ta 0:00:011
Requirement already satisfied (use --upgrade to upgrade): Flask>=0.7 in c:\swat\.virtualenvs\monkblog\lib\site-packages (from Flask-Misaka)
Collecting misaka (from Flask-Misaka)
  Downloading misaka-1.0.2.tar.gz (78kB)
    100% |################################| 81kB 744kB/s ta 0:00:011
Requirement already satisfied (use --upgrade to upgrade): Werkzeug>=0.7 in c:\swat\.virtualenvs\monkblog\lib\site-packages (from Flask>=0.7->Flask-Misaka)
Requirement already satisfied (use --upgrade to upgrade): Jinja2>=2.4 in c:\swat\.virtualenvs\monkblog\lib\site-packages (from Flask>=0.7->Flask-Misaka)
Requirement already satisfied (use --upgrade to upgrade): itsdangerous>=0.21 in c:\swat\.virtualenvs\monkblog\lib\site-packages (from Flask>=0.7->Flask-Misaka)
Requirement already satisfied (use --upgrade to upgrade): MarkupSafe in c:\swat\.virtualenvs\monkblog\lib\site-packages (from Jinja2>=2.4->Flask>=0.7->Flask-Misaka)
Installing collected packages: misaka, Flask-Misaka
  Running setup.py install for misaka
    building 'misaka' extension
    error: Microsoft Visual C++ 10.0 is required (Unable to find vcvarsall.bat).
    Complete output from command c:\Swat\.virtualenvs\monkblog\Scripts\python3.exe -c "import setuptools, tokenize;__file__='C:\\Users\\PITTMA~1\\AppData\\Local\\Temp\\pip-build-val0j4kr\\misaka\\setup.py';exec(compile(getattr(tokenize, 'open', open)(__file__).read().replace('\r\n', '\n'), __file__, 'exec'))" install --record C:\Users\PITTMA~1\AppData\Local\Temp\pip-opg0fnev-record\install-record.txt --single-version-externally-managed --compile --install-headers c:\Swat\.virtualenvs\monkblog\include\site\python3.4:
    running install

    running build

    running build_ext

    building 'misaka' extension

    error: Microsoft Visual C++ 10.0 is required (Unable to find vcvarsall.bat).
    ----------------------------------------
    Command "c:\Swat\.virtualenvs\monkblog\Scripts\python3.exe -c "import setuptools, tokenize;__file__='C:\\Users\\PITTMA~1\\AppData\\Local\\Temp\\pip-build-val0j4kr\\misaka\\setup.py';exec(compile(getattr(tokenize, 'open', open)(__file__).read().replace('\r\n', '\n'), __file__, 'exec'))" install --record C:\Users\PITTMA~1\AppData\Local\Temp\pip-opg0fnev-record\install-record.txt --single-version-externally-managed --compile --install-headers c:\Swat\.virtualenvs\monkblog\include\site\python3.4" failed with error code 1 in C:\Users\PITTMA~1\AppData\Local\Temp\pip-build-val0j4kr\misaka
