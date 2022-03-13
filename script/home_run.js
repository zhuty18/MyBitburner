/** @param {NS} ns **/
export async function main (ns) {
    ns.exec("get.js", "home", 1)
    await ns.asleep(1000)
    ns.exec("scan.js", "home", 1)
}