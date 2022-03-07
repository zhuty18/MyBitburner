/** @param {NS} ns **/
export async function main (ns) {
    var filename = [
        "basic", "easy_loop", "find", "grow", "hack", "refresh",
        "scan", "weaken", "prepare", "foo", "join"
    ]
    for (var i = 0; i < filename.length; i++) {
        var n = filename[i] + ".js"
        ns.rm(n)
        var success = await ns.wget("http://127.0.0.1:8000/script/" + n, n)
        if (success) {
            ns.print("success download " + n)
        }
        else {
            ns.print("failed download " + n)
        }
    }
}