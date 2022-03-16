/** @param {NS} ns **/
export async function main (ns) {
    var target = ns.args[0]
    var cores = 4
    while (true) {
        var max_money = ns.getServerMaxMoney(target)
        var ava_money = ns.getServerMoneyAvailable(target)
        var g_time = ns.getGrowTime(target)
        var w_time = ns.getWeakenTime(target)
        var h_time = ns.getHackTime(target)
        var th_g = ns.growthAnalyze(target, max_money / ava_money, cores)
        var th_h = ns.hackAnalyzeThreads(target, max_money)
        var th_w_g = ns.growthAnalyzeSecurity(th_g) / 0.05
        var th_w_h = ns.hackAnalyzeSecurity(th_h) / 0.05
        ns.print(max_money + " " + ava_money)
        ns.print(th_g + " " + th_w_g)
        ns.print(th_h + " " + th_w_h)
        if (th_g > 0) {
            ns.run("grow.js", th_g, target)
            await ns.asleep(g_time - w_time + 200)
            ns.run("weaken.js", th_w_g, target)
            await ns.asleep(400)
        }
        ns.run("weaken.js", th_w_h, target)
        await ns.asleep(w_time - h_time - 200)
        ns.run("hack.js", th_h, target)
    }
}