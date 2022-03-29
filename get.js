/** @param {NS} ns **/
export async function main (ns) {
    var filename = [
        "easy_loop", "find", "grow", "hack", "scan", "weaken", "share", "share_count"
    ]
    for (var i = 0; i < filename.length; i++) {
        var n = filename[i] + ".js"
        ns.rm(n)
        var success = await ns.wget("http://127.0.0.1:8080/script/" + n, n)
        if (success) {
            ns.print("success download " + n)
        }
        else {
            ns.print("failed download " + n)
        }
    }
}