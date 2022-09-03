async function main() {
    let pyodide = await loadPyodide();
    // await pyodide.loadPackage('pydantic');
    await pyodide.loadPackage('micropip')
    // await pyodide.loadPackage(['pydantic','numpy','pandas','scikit-learn']);
    const micropip = pyodide.pyimport("micropip");
    await micropip.install(['pydantic']);
    // await micropip.install(['pydantic','altair','numpy','pandas','scikit-learn','panel==0.13.1']);

    // Pyodide is now ready to use...
    pyodide.runPythonAsync(`
import sys
print(f'sys.version={sys.version}')
import pydantic
print(f'pydantic={pydantic.__version__}')
# Run this using "asyncio"

from pathlib import Path
from pyodide.http import pyfetch


response = await pyfetch('client_bundle.zip')
await response.unpack_archive()

import sys
sys.path.insert(0, str(Path('./additional').absolute()))

import app.browser.main as m
await m.main()
  `);
}

main();