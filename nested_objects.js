var obj = {"a": { "b": { "c": "d" }}};
var obj = {"x": { "y": { "z": "a" }}};

function getObjectKeys(object, key) {
    const keys = key.split('.');
    let obj = object;
    for (let ikey of keys) {
        for (let [objKey, value] of Object.entries(obj)) {
            if(!keys.includes(objKey)) {
                continue;
            }
            obj = value;
        }
    }
    return obj;
}
