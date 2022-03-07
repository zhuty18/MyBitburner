/** @param {NS} ns **/

function str (len) {
    var s = ""
    for (var i = 0; i < len; i++) {
        s += "-"
    }
    return s
}

function res (ns, father, current, target, depth) {
    if (current == target) {
        ns.print(str(depth) + target)
        return true
    }
    var l = ns.scan(current)
    for (var i = 0; i < l.length; i++) {
        if (l[i] != father) {
            var t = res(ns, current, l[i], target, depth + 2)
            if (t) {
                ns.print(str(depth) + current)
                return true
            }
        }
    }
    return false
}
export async function main (ns) {
    ns.disableLog("scan")
    var target = ns.args[0]
    res(ns, "", "home", target, 0)
}