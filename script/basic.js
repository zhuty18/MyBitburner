/** @param {NS} ns **/
export async function main (ns) {
    var target = ns.args[0]
    var ram = ns.args[1]
    var chance = ns.hackAnalyzeChance(target);
    var grow_time = ns.getGrowTime(target);
    var hack_time = ns.getHackTime(target);
    var weaken_time = ns.getWeakenTime(target);
    var grow_money = ns.getServerGrowth(target) * ns.getServerMoneyAvailable(target);
    var hack_money = ns.hackAnalyze(target) * chance;
    var grow_thread = (hack_money * grow_time) / (grow_money * hack_time);
    var grow_security = grow_thread * 0.004;
    var hack_security = chance * 0.002;
    var weaken_thread_g = (grow_security * weaken_time) / (0.05 * grow_time);
    var weaken_thread_h = (hack_security * weaken_time) / (0.05 * hack_time);
    var ram_use = 1.7 + (weaken_thread_g + weaken_thread_h + grow_thread) * 1.75
    var m = ram / ram_use
    var hack_t = m
    var grow_t = grow_thread * m
    var weaken_t_g = weaken_thread_g * m
    var weaken_t_h = weaken_thread_h * m
    var ale = "hack thread: " + hack_t + "\n"
    ale += "grow thread: " + grow_t + "\n"
    ale += "weaken_g thread: " + weaken_t_g + "\n"
    ale += "weaken_h thread: " + weaken_t_h + "\n"
    ns.alert(ale)
}