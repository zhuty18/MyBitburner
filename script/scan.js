/** @param {NS} ns **/

export async function main (ns) {
    ns.disableLog("scan");
    ns.disableLog("scp");
    ns.disableLog("getServerRequiredHackingLevel");
    ns.disableLog("getServerMaxRam");
    ns.disableLog("getServerNumPortsRequired");
    ns.disableLog("asleep");
    while (true) {
        await loop(ns, "home", 0, "");
        await ns.asleep(30000);
    }
}
async function attack (ns, a) {
    var keys = 0
    if (ns.fileExists("brutessh.exe")) {
        keys++
        if (ns.fileExists("ftpcrack.exe")) {
            keys++
            if (ns.fileExists("relaysmtp.exe")) {
                keys++
                if (ns.fileExists("httpworm.exe")) {
                    keys++
                    if (ns.fileExists("sqlinject.exe")) {
                        keys++
                    }
                }
            }

        }
    }
    if (ns.getServerNumPortsRequired(a) <= keys) {
        ns.print("attack: " + a)
        if (keys > 0) {
            ns.brutessh(a);
            if (keys > 1) {
                ns.ftpcrack(a);
                if (keys > 2) {
                    ns.relaysmtp(a);
                    if (keys > 3) {
                        ns.httpworm(a);
                        if (keys > 4) {
                            ns.sqlinject(a);
                        }
                    }
                }
            }

        }
        ns.nuke(a);
        await ns.scp(["basic.js", "easy_loop.js", "hack.js", "grow.js", "weaken.js", "prepare.js"], a);
        var ram = ns.getServerMaxRam(a)
        ns.tprint("get access of " + a + " " + ram)
        ns.print("get access of " + a + "!")
        if (ram != 0) {
            var target = a
            if (target == "CSEC" || target == "avmnite-02h") {
                target = "n00dles"
            }
            else if (target == "I.I.I.I") {
                target = "crush-fitness"
            }
            else if (target == "run4theh111z") {
                target = "crush-fitness"
            }
            ns.exec("easy_loop.js", a, 1, target, ram)
        }
    }
}

function str (len, a) {
    var res = ""
    for (var i = 0; i < len - 2; i++) {
        res += " "
    }
    res += "|-" + a
    return res
}

async function loop (ns, a, len, father) {
    if (!ns.hasRootAccess(a)) {
        await attack(ns, a);
    }
    // ns.print(str(len,a))
    var t = ns.ls(a, "cct");
    if (t.length != 0) {
        ns.alert("code contract on " + a + "!");
        ns.tprint("code contract on " + a + "!");
        ns.print("code contract on " + a + "!");
    }
    var h = ns.scan(a);
    var l = h.length;
    for (var i = 0; i < l; i++) {
        if (h[i] != father) {
            var target = h[i];
            await loop(ns, target, len + 2, a);
        }
    }
}