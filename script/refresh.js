/** @param {NS} ns **/
export async function main (ns) {
	var target = ns.args[0]
	if (ns.fileExists("brutessh.exe")) {
		ns.brutessh(target);
		if (ns.fileExists("ftpcrack.exe")) {
			ns.ftpcrack(target);
			if (ns.fileExists("relaysmtp.exe")) {
				ns.relaysmtp(target);
				if (ns.fileExists("httpworm.exe")) {
					ns.httpworm(target);
					if (ns.fileExists("sqlinject.exe")) {
						ns.sqlinject(target);
					}
				}
			}

		}
	}
	ns.nuke(target);
	await ns.scp("basic.js", target);
	await ns.scp("easy_loop.js", target);
	await ns.scp("hack.js", target);
	await ns.scp("grow.js", target);
	await ns.scp("weaken.js", target);
	await ns.scp("prepare.js", target);
}