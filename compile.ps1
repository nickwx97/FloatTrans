python -m nuitka `
--onefile .\src\main.py `
--windows-uac-admin `
--output-filename=FloatTrans `
--enable-plugin=tk-inter `
--remove-output `
--windows-console-mode=disable