/** @param {NS} ns **/
export async function main (ns) {
    var h = ns.args[0]
    var ram = ns.args[1]
    var num = ns.args[2]
    var pur = ns.args[3]
    ns.print(ns.getPurchasedServerCost(ram))
    for (var i = 0; i < num; i++) {
        var target = h + "_" + i
        if (pur != null) {
            ns.purchaseServer(target, ram);
        }
        await ns.scp(["basic.js", "easy_loop.js", "hack.js", "grow.js", "weaken.js", "prepare.js"], target);
        ns.exec("easy_loop.js", target, 1, h, ram)
    }
}