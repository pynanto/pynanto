if (typeof pyodide_src_url === 'undefined')
    pyodide_src_url = 'https://cdn.jsdelivr.net/pyodide/v0.21.2/full/pyodide.js'

async function main() {
    if (typeof loadPyodide === 'undefined') {
        async function load_script(src) {
            let script = document.createElement('script');
            script.src = src;
            let resolve = '';
            let promise = new Promise(r => resolve = r);
            script.onload = () => resolve();
            document.body.append(script)
            await promise;
        }

        await load_script(pyodide_src_url);
    }
    let pyodide = await loadPyodide();
    await pyodide.loadPackage('micropip')
    const micropip = pyodide.pyimport("micropip");
    await micropip.install(['pydantic']);
    pyodide.runPythonAsync(`
import sys
import pydantic

from pathlib import Path
from pyodide.http import pyfetch


response = await pyfetch('client_bundle.zip')
await response.unpack_archive()

sys.path.insert(0, str(Path('./additional').absolute()))

import app.browser.main as m
await m.main()
  `);
}

main();