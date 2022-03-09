/** @param {NS} ns **/
export async function main (ns) {
    var target = ns.args[0]
    var ram = ns.args[1]
    var gw = (ram - 3.15) / 1.75
    var h = (ram - 3.15) / 1.7
    while (true) {
        if ((ns.getServerMoneyAvailable(target) / ns.getServerMaxMoney(target)) < 0.05) {
            ns.run("grow.js", gw, target)
            await ns.asleep(ns.getGrowTime(target) + 1000)
        }
        else if ((ns.getServerSecurityLevel(target) - gw * 0.05) / ns.getServerMinSecurityLevel(target) > 5) {
            ns.run("weaken.js", gw, target)
            await ns.asleep(ns.getWeakenTime(target) + 1000)
        }
        else {
            ns.run("hack.js", h, target)
            await ns.asleep(ns.getHackTime(target) + 1000)
        }
    }
}