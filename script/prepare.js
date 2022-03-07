/** @param {NS} ns **/
export async function main (ns) {
    var target = ns.args[0]
    var ram = ns.args[1]
    var gw = (ram - 3.1) / 1.75
    while (true) {
        if ((ns.getServerMaxMoney(target) / ns.getServerMoneyAvailable(target)) * 100 - 100 > ns.getServerGrowth(target) * gw) {
            ns.print(ns.getServerMaxMoney(target))
            ns.print(ns.getServerMoneyAvailable(target))
            ns.run("grow.js", gw, target)
        }
        else if ((ns.getServerSecurityLevel(target) - ns.getServerMinSecurityLevel(target)) > gw * 0.05) {
            ns.run("weaken.js", gw, target)
        }
        else {
            ns.tprint(target + "prepared! ")
            break
        }
        await ns.sleep(1000)
    }
}