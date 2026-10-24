import ipaddress
import os
import re
import socket
import sys
import textwrap

import requests


VERSION = "1.1.0"
AUTHOR = "Vikas Singh"

IP_API = "https://ipwho.is"
RDAP_API = "https://rdap.org/ip"


# ─────────────────────────────────────────────────────────────
# COLORS
# ─────────────────────────────────────────────────────────────

RESET = "\033[0m"
BOLD = "\033[1m"

BANNER = "\033[38;5;129m"      # Electric Purple
WHITE = "\033[97m"
SHADOW = "\033[37m"

BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"


# ─────────────────────────────────────────────────────────────
# UI SETTINGS
# ─────────────────────────────────────────────────────────────

BOX_WIDTH = 72
LABEL_WIDTH = 18


# ─────────────────────────────────────────────────────────────
# TERMINAL
# ─────────────────────────────────────────────────────────────

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# ─────────────────────────────────────────────────────────────
# BANNER
# ─────────────────────────────────────────────────────────────

def banner():

    logo = [
        "╔════════════════════════════════════════════════════════════╗",
        "║                                                            ║",
        "║   ██╗██████╗       ██╗███╗   ██╗████████╗███████╗██╗      ║",
        "║   ██║██╔══██╗      ██║████╗  ██║╚══██╔══╝██╔════╝██║      ║",
        "║   ██║██████╔╝█████╗██║██╔██╗ ██║   ██║   █████╗  ██║      ║",
        "║   ██║██╔═══╝ ╚════╝██║██║╚██╗██║   ██║   ██╔══╝  ██║      ║",
        "║   ██║██║           ██║██║ ╚████║   ██║   ███████╗██║      ║",
        "║   ╚═╝╚═╝           ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝      ║",
        "║                                                            ║",
        "║                     I P - I N T E L                        ║",
        "║                                                            ║",
        "╚════════════════════════════════════════════════════════════╝",
    ]

    for line in logo:
        print(" " + SHADOW + line + RESET)

    print(f"\033[{len(logo)}A", end="")

    for line in logo:
        print(BANNER + BOLD + line + RESET)

    print(
        GRAY
        + "────────────────────────────────────────────────────────────"
        + RESET
    )

    print(f" {BLUE}Version{RESET} : {WHITE}{VERSION}{RESET}")
    print(f" {BLUE}Author {RESET} : {WHITE}{AUTHOR}{RESET}")
    print(
        f" {BLUE}Purpose{RESET} : "
        f"{WHITE}Public IP intelligence & reconnaissance{RESET}"
    )

    print(
        GRAY
        + "────────────────────────────────────────────────────────────"
        + RESET
    )

    print()


# ─────────────────────────────────────────────────────────────
# HELP
# ─────────────────────────────────────────────────────────────

def show_help():

    print()

    print(f"{BANNER}{BOLD}COMMANDS{RESET}")

    print(
        GRAY
        + "────────────────────────────────────────────────────────"
        + RESET
    )

    print(f"  {WHITE}<IP>{RESET}       Analyze an IP address")
    print(f"  {WHITE}help{RESET}      Show available commands")
    print(f"  {WHITE}clear{RESET}     Clear the terminal")
    print(f"  {WHITE}version{RESET}   Show IP-INTEL version")
    print(f"  {WHITE}exit{RESET}      Exit IP-INTEL")

    print()

    print(f"{BANNER}{BOLD}EXAMPLES{RESET}")

    print(
        GRAY
        + "────────────────────────────────────────────────────────"
        + RESET
    )

    print(f"  {WHITE}8.8.8.8{RESET}")
    print(f"  {WHITE}1.1.1.1{RESET}")
    print(f"  {WHITE}14.142.39.94{RESET}")
    print(f"  {WHITE}2001:4860:4860::8888{RESET}")

    print()


# ─────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────

def safe_value(value):

    if value is None:
        return "Unknown"

    if value == "":
        return "Unknown"

    return str(value)


def yes_no(value):

    if value is True:
        return f"{GREEN}YES{RESET}"

    if value is False:
        return f"{RED}NO{RESET}"

    return f"{YELLOW}UNKNOWN{RESET}"


def ip_type(data):

    if data["private"]:
        return f"{YELLOW}PRIVATE{RESET}"

    if data["global"]:
        return f"{GREEN}PUBLIC{RESET}"

    return f"{YELLOW}NON-GLOBAL{RESET}"


def strip_ansi(text):

    ansi_pattern = re.compile(
        r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])"
    )

    return ansi_pattern.sub("", str(text))


# ─────────────────────────────────────────────────────────────
# UI SECTIONS
# ─────────────────────────────────────────────────────────────

def section(title):

    print()

    print(
        f"{BANNER}╭{'─' * BOX_WIDTH}╮{RESET}"
    )

    title_text = f" {title}"

    print(
        f"{BANNER}│{RESET}"
        f"{BOLD}{WHITE}{title_text:<{BOX_WIDTH}}{RESET}"
        f"{BANNER}│{RESET}"
    )

    print(
        f"{BANNER}├{'─' * BOX_WIDTH}┤{RESET}"
    )


def row(label, value):

    label_text = f"{label:<{LABEL_WIDTH}}"
    value_text = str(value)

    visible_value = strip_ansi(value_text)

    used_width = 1 + LABEL_WIDTH + 3 + len(visible_value)

    padding = BOX_WIDTH - used_width

    if padding < 1:
        padding = 1

    print(
        f"{BANNER}│{RESET} "
        f"{BLUE}{label_text}{RESET}"
        f" : "
        f"{value_text}"
        f"{' ' * padding}"
        f"{BANNER}│{RESET}"
    )


def wrapped_row(label, value):

    value_text = str(value)
    visible_value = strip_ansi(value_text)

    available_width = (
        BOX_WIDTH
        - 1
        - LABEL_WIDTH
        - 3
    )

    if len(visible_value) <= available_width:

        row(label, value)
        return

    wrapped = textwrap.wrap(
        visible_value,
        width=available_width
    )

    for index, line in enumerate(wrapped):

        if index == 0:

            row(label, line)

        else:

            padding = BOX_WIDTH - 1 - len(line)

            print(
                f"{BANNER}│{RESET} "
                f"{' ' * (LABEL_WIDTH + 3)}"
                f"{WHITE}{line}{RESET}"
                f"{' ' * padding}"
                f"{BANNER}│{RESET}"
            )


def section_end():

    print(
        f"{BANNER}╰{'─' * BOX_WIDTH}╯{RESET}"
    )


# ─────────────────────────────────────────────────────────────
# LOCAL IP ANALYSIS
# ─────────────────────────────────────────────────────────────

def analyze_local_ip(ip):

    try:

        ip_obj = ipaddress.ip_address(ip)

    except ValueError:

        return None

    return {
        "address": str(ip_obj),
        "version": f"IPv{ip_obj.version}",
        "private": ip_obj.is_private,
        "global": ip_obj.is_global,
        "loopback": ip_obj.is_loopback,
        "multicast": ip_obj.is_multicast,
        "link_local": ip_obj.is_link_local,
        "reserved": ip_obj.is_reserved,
    }


# ─────────────────────────────────────────────────────────────
# REVERSE DNS
# ─────────────────────────────────────────────────────────────

def reverse_dns(ip):

    try:

        hostname, _, _ = socket.gethostbyaddr(ip)

        return hostname

    except (socket.herror, socket.gaierror, OSError):

        return "Not found"


# ─────────────────────────────────────────────────────────────
# IP INTELLIGENCE API
# ─────────────────────────────────────────────────────────────

def get_ip_intelligence(ip):

    url = f"{IP_API}/{ip}"

    headers = {
        "User-Agent": "IP-INTEL/1.1"
    }

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if not data.get("success", False):

            return None, data.get(
                "message",
                "API returned an error"
            )

        return data, None

    except requests.exceptions.Timeout:

        return None, "Request timed out"

    except requests.exceptions.ConnectionError:

        return None, "Connection failed"

    except requests.exceptions.HTTPError as error:

        return None, f"HTTP error: {error}"

    except requests.exceptions.RequestException as error:

        return None, f"Request failed: {error}"

    except ValueError:

        return None, "Invalid JSON response"


# ─────────────────────────────────────────────────────────────
# RDAP
# ─────────────────────────────────────────────────────────────

def get_rdap(ip):

    url = f"{RDAP_API}/{ip}"

    headers = {
        "User-Agent": "IP-INTEL/1.1"
    }

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        response.raise_for_status()

        return response.json(), None

    except requests.exceptions.Timeout:

        return None, "RDAP request timed out"

    except requests.exceptions.ConnectionError:

        return None, "RDAP connection failed"

    except requests.exceptions.HTTPError as error:

        return None, f"RDAP HTTP error: {error}"

    except requests.exceptions.RequestException as error:

        return None, f"RDAP request failed: {error}"

    except ValueError:

        return None, "Invalid RDAP response"


# ─────────────────────────────────────────────────────────────
# RDAP ENTITY PARSER
# ─────────────────────────────────────────────────────────────

def parse_entity(entity):

    result = {}

    if not entity:
        return result

    roles = entity.get("roles", [])

    if roles:
        result["role"] = ", ".join(roles)

    vcard = entity.get("vcardArray")

    if not isinstance(vcard, list):
        return result

    if len(vcard) < 2:
        return result

    fields = vcard[1]

    for field in fields:

        if not isinstance(field, list):
            continue

        if len(field) < 4:
            continue

        field_name = field[0]
        field_value = field[3]

        if field_name == "fn":

            result["name"] = field_value

        elif field_name == "email":

            result["email"] = field_value

        elif field_name == "tel":

            result["phone"] = field_value

    return result


# ─────────────────────────────────────────────────────────────
# ABUSE CONTACT
# ─────────────────────────────────────────────────────────────

def get_abuse_contact(rdap):

    entities = rdap.get("entities", [])

    for entity in entities:

        roles = entity.get("roles", [])

        if "abuse" in roles:

            return parse_entity(entity)

    return {}


# ─────────────────────────────────────────────────────────────
# DISPLAY TARGET
# ─────────────────────────────────────────────────────────────

def display_target(local):

    section("TARGET")

    row("IP Address", local["address"])
    row("IP Version", local["version"])
    row("Type", ip_type(local))
    row("Global", yes_no(local["global"]))
    row("Loopback", yes_no(local["loopback"]))

    section_end()


# ─────────────────────────────────────────────────────────────
# DISPLAY DNS
# ─────────────────────────────────────────────────────────────

def display_dns(hostname):

    section("DNS")

    wrapped_row("Reverse DNS", hostname)
    wrapped_row("PTR", hostname)

    section_end()


# ─────────────────────────────────────────────────────────────
# DISPLAY NETWORK
# ─────────────────────────────────────────────────────────────

def display_network(data):

    connection = data.get("connection") or {}

    section("NETWORK")

    asn = connection.get("asn")

    if asn:

        asn_text = str(asn)

        if not asn_text.upper().startswith("AS"):

            asn_text = f"AS{asn_text}"

    else:

        asn_text = "Unknown"

    row("ASN", asn_text)

    wrapped_row(
        "Organization",
        safe_value(connection.get("org"))
    )

    wrapped_row(
        "ISP",
        safe_value(connection.get("isp"))
    )

    wrapped_row(
        "Domain",
        safe_value(connection.get("domain"))
    )

    section_end()


# ─────────────────────────────────────────────────────────────
# GEOLOCATION
# ─────────────────────────────────────────────────────────────

def display_geolocation(data):

    section("GEOLOCATION")

    row(
        "Country",
        safe_value(data.get("country"))
    )

    row(
        "Country Code",
        safe_value(data.get("country_code"))
    )

    row(
        "Region",
        safe_value(data.get("region"))
    )

    row(
        "City",
        safe_value(data.get("city"))
    )

    row(
        "Postal Code",
        safe_value(data.get("postal"))
    )

    latitude = safe_value(
        data.get("latitude")
    )

    longitude = safe_value(
        data.get("longitude")
    )

    row(
        "Coordinates",
        f"{latitude}, {longitude}"
    )

    timezone = data.get("timezone") or {}

    row(
        "Timezone",
        safe_value(timezone.get("id"))
    )

    section_end()


# ─────────────────────────────────────────────────────────────
# SECURITY
# ─────────────────────────────────────────────────────────────

def display_security(data):

    security = data.get("security") or {}

    section("SECURITY / REPUTATION")

    row(
        "VPN",
        yes_no(security.get("vpn"))
    )

    row(
        "Proxy",
        yes_no(security.get("proxy"))
    )

    row(
        "Tor",
        yes_no(security.get("tor"))
    )

    row(
        "Hosting",
        yes_no(security.get("hosting"))
    )

    section_end()


# ─────────────────────────────────────────────────────────────
# OWNERSHIP
# ─────────────────────────────────────────────────────────────

def display_ownership(rdap):

    section("OWNERSHIP")

    wrapped_row(
        "Handle",
        safe_value(rdap.get("handle"))
    )

    wrapped_row(
        "Network Name",
        safe_value(rdap.get("name"))
    )

    row(
        "Start Address",
        safe_value(rdap.get("startAddress"))
    )

    row(
        "End Address",
        safe_value(rdap.get("endAddress"))
    )

    row(
        "Country",
        safe_value(rdap.get("country"))
    )

    row(
        "Registry",
        safe_value(rdap.get("port43"))
    )

    section_end()


# ─────────────────────────────────────────────────────────────
# ABUSE CONTACT
# ─────────────────────────────────────────────────────────────

def display_abuse(rdap):

    abuse = get_abuse_contact(rdap)

    section("ABUSE CONTACT")

    if not abuse:

        row(
            "Status",
            f"{YELLOW}Not available{RESET}"
        )

        section_end()

        return

    wrapped_row(
        "Name",
        safe_value(abuse.get("name"))
    )

    wrapped_row(
        "Email",
        safe_value(abuse.get("email"))
    )

    wrapped_row(
        "Phone",
        safe_value(abuse.get("phone"))
    )

    section_end()


# ─────────────────────────────────────────────────────────────
# MAIN RECON
# ─────────────────────────────────────────────────────────────

def analyze_ip(ip):

    local = analyze_local_ip(ip)

    if local is None:

        print(
            f"\n{RED}[!] Invalid IP address: "
            f"{ip}{RESET}\n"
        )

        return

    print()

    print(
        f"{GREEN}[+] Target accepted:{RESET} "
        f"{WHITE}{ip}{RESET}"
    )

    print()

    print(
        f"{GRAY}[*] Running IP reconnaissance...{RESET}"
    )

    print(
        f"{GRAY}    ├─ Target analysis{RESET}"
    )

    display_target(local)

    hostname = reverse_dns(ip)

    if not local["global"]:

        print()

        print(
            f"{YELLOW}[!] Non-public IP detected.{RESET}"
        )

        print(
            f"{GRAY}[*] Public intelligence lookup skipped."
            f"{RESET}"
        )

        print()

        return

    print(
        f"{GRAY}[*] Querying IP intelligence source...{RESET}"
    )

    data, api_error = get_ip_intelligence(ip)

    if data:

        # Important intelligence first
        display_geolocation(data)
        display_network(data)

    else:

        print()

        print(
            f"{YELLOW}[!] IP intelligence unavailable:{RESET} "
            f"{api_error}"
        )

    print(
        f"{GRAY}[*] Querying RDAP ownership data...{RESET}"
    )

    rdap, rdap_error = get_rdap(ip)

    if rdap:

        display_ownership(rdap)

    else:

        print()

        print(
            f"{YELLOW}[!] RDAP unavailable:{RESET} "
            f"{rdap_error}"
        )

    # Secondary intelligence
    display_security(data if data else {})
    display_dns(hostname)

    if rdap:
        display_abuse(rdap)

    print()

    print(
        f"{GREEN}[+] Reconnaissance complete.{RESET}"
    )

    print(
        GRAY
        + "────────────────────────────────────────────────────────────"
        + RESET
    )

    print()


# ─────────────────────────────────────────────────────────────
# VERSION
# ─────────────────────────────────────────────────────────────

def show_version():

    print()

    print(
        f"{BANNER}{BOLD}IP-INTEL{RESET} "
        f"{WHITE}v{VERSION}{RESET}"
    )

    print(
        f"{GRAY}Author: {AUTHOR}{RESET}"
    )

    print()


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────

def main():

    clear_screen()

    banner()

    print(
        f"{GRAY}Type 'help' for available commands.{RESET}\n"
    )

    while True:

        try:

            command = input(
                f"{BANNER}{BOLD}ENTER-IP{RESET} "
                f"{GREEN}❯{RESET} "
            ).strip()

            if not command:
                continue

            command_lower = command.lower()

            if command_lower in (
                "exit",
                "quit",
                "q"
            ):

                print()

                print(
                    f"{GREEN}[+] IP-INTEL terminated.{RESET}"
                )

                print()

                sys.exit(0)

            elif command_lower in (
                "help",
                "?"
            ):

                show_help()

            elif command_lower == "clear":

                clear_screen()

                banner()

            elif command_lower == "version":

                show_version()

            else:

                analyze_ip(command)

        except KeyboardInterrupt:

            print()

            print(
                f"{GREEN}[+] IP-INTEL terminated.{RESET}"
            )

            print()

            sys.exit(0)

        except EOFError:

            print()

            print(
                f"{GREEN}[+] IP-INTEL terminated.{RESET}"
            )

            print()

            sys.exit(0)


# ─────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()