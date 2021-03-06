/** @param {NS} ns **/
export async function main (ns) {
    var target = ns.args[0]
    var ram = ns.args[1]
    var gw = (ram - 3.3) / 1.75
    var h = (ram - 3.3) / 1.7
    while (true) {
        var ava_money = ns.getServerMoneyAvailable(target)
        var max_money = ns.getServerMaxMoney(target)
        if (((ava_money / max_money) - gw * 0.005 < 0.05) && (ava_money != max_money)) {
            ns.run("grow.js", gw, target)
            await ns.asleep(ns.getGrowTime(target) + 1000)
        }
        else if ((ns.getServerSecurityLevel(target) - gw * 0.05) > ns.getServerMinSecurityLevel(target)) {
            ns.run("weaken.js", gw, target)
            await ns.asleep(ns.getWeakenTime(target) + 1000)
        }
        else {
            if (ns.getServerRequiredHackingLevel(target) <= ns.getHackingLevel()) {
                ns.run("hack.js", h, target)
                await ns.asleep(ns.getHackTime(target) + 1000)
            }
            else {
                ns.run("grow.js", gw, target)
                await ns.asleep(ns.getGrowTime(target) + 1000)
            }
        }
    }
}