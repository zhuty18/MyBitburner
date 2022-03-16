/** @param {NS} ns **/
export async function main (ns) {
    var fre = ns.args[0]
    ns.disableLog("scan");
    ns.disableLog("scp");
    ns.disableLog("getServerRequiredHackingLevel");
    ns.disableLog("getServerMaxRam");
    ns.disableLog("getServerNumPortsRequired");
    ns.disableLog("asleep");
    if (fre != null) {
        await loop(ns, fre, "home", 0, "")
    }
    else {
        while (true) {
            await loop(ns, null, "home", 0, "");
            await ns.asleep(30000);
        }
    }
}
async function fresh (ns, a, fre) {
    await ns.scp(["basic.js", "easy_loop.js", "hack.js", "grow.js", "weaken.js", "prepare.js"], a);
    var ram = ns.getServerMaxRam(a)
    if (a.search("--") != -1) {
        var target = a.split("--")[0]
        ns.exec("easy_loop.js", a, 1, target, ram)
    }
    else {
        ns.tprint("get access of " + a + " " + ram)
        ns.print("get access of " + a + "!")
        if (ram != 0) {
            var target = a
            if (target == "CSEC") {
                // await ns.installBackdoor(target);
                target = "n00dles"
            }
            else if (target == "avmnite-02h") {
                target = "n00dles"
            }
            else if (target == "I.I.I.I") {
                // await ns.installBackdoor(target);
                target = "n00dles"
            }
            else if (target == "run4theh111z") {
                // await ns.installBackdoor(target);
                target = "n00dles"
            }
            else if (target == ".") {
                // await ns.installBackdoor(target);
                target = "n00dles"
            }
            else if (target == "The-Cave") {
                // await ns.installBackdoor(target);
                target = "n00dles"
            }
            if (ram <= 8) {
                await ns.scp(["share.js"], a);
                ns.exec("share.js", a, ram / 4)
            }
            if (target != "home") {
                ns.exec("easy_loop.js", a, 1, target, ram)
                if (ram <= 32) {
                    var r = ns.getServerMaxRam("home")
                    ns.exec("easy_loop.js", "home", 1, target, r / 16 - 1)
                    ns.tprint("home hacking " + target)
                }
            }
        }
        else {
            var l1 = ["The-Cave"]
            var have = false
            for (var i = 0; i < l1.length; i++) {
                if (a == l1[i]) {
                    have = true
                    break
                }
            }
            if (!have) {
                var l2 = ns.getPurchasedServers();
                for (var j = 0; j < fre; j++) {
                    var purchased = false
                    var h = a + "--" + j
                    for (var i = 0; i < l2.length; i++) {
                        if (h == l2[i]) {
                            purchased = true
                            break
                        }
                    }
                    if (!purchased) {
                        if (await ns.prompt("buy server by " + ns.getPurchasedServerCost(1024) / 1000000 + "m?")) {
                            ns.purchaseServer(h, 1024);
                            ns.tprint("bought server " + h + "!")
                            await ns.scp(["basic.js", "easy_loop.js", "hack.js", "grow.js", "weaken.js", "prepare.js"], h);
                            ns.exec("easy_loop.js", h, 1, a, 1024)
                        }
                    }
                }
            }
        }
    }
}
async function attack (ns, a, fre) {
    if (a.search("_") != -1) {
        await fresh(ns, a, fre);
    }
    else {
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
            await fresh(ns, a, fre);
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

async function loop (ns, fre, a, len, father) {
    if ((!ns.hasRootAccess(a)) || (fre != null)) {
        await attack(ns, a, fre);
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
            await loop(ns, fre, target, len + 2, a);
        }
    }
}
