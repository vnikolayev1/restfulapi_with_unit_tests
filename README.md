`pip install pipenv`in console
`pip install` in project's folder to download all packages i used.
To activate this project's virtualenv, run `pipenv shell`
`export FLASK_APP=api.py` (unix) or 
`$env:FLASK_APP = "api.py"`(powershell)
`set FLASK_APP=api.py` (windows cmd) to let flask know what file to start with.
`pytest` to run unit tests on program
`flask run` to run server

Task specification

POST:  /api/multiply
Takes two paramaters `number` and `times`. Returns number multiplyed on itself `times` times.

POST:  /api/group
Takes one parameter `words` which recieves words divided by comma. In the end it groups  words by range from 2nd to 4th letter of the word. Example: `( word, lord, master, keys, foot, loot)`  `word` and `lord` have same letters on positions 2-4 `(ORD)`, `foot` and `loot` has `(OOT)`. In the end we return grouped words as list of lists -> `[ [word, lord], [foot, loot], [keys], [master] ]`

POST:  /api/serialize
Serialize text, sent as `text` parameter. Serialization is simple. From text `“hello -> brave -> new world”` we recieve `“{‘hello’: {‘brave’: {‘new world’: ‘’}}}”` Apply few tests to check unexpected situations and program's logic.
