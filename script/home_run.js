/** @param {NS} ns **/
export async function main (ns) {
    ns.exec("get.js", "home", 1)
    await ns.asleep(1000)
    ns.exec("scan.js", "home", 1)
    var ram = ns.getServerMaxRam("home")
    var l = ["foodnstuff", "zer0", "sigma-cosmetics", "max-hardware", "joesguns", "nectar-net", "hong-fang-tea", "harakiri-sushi", "iron-gym", "neo-net"]
    for (var i = 0; ((i < l.length) && ((i + 1) * 1024 <= ram)); i++) {
        ns.exec("easy_loop.js", "home", 1, l[i], 1020)
    }
}