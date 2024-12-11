import os
import subprocess
import time
import json
from threading import Thread

# Globale Variablen
xmrig_logs = []  # Log-Speicher
mining_status = "Inactive"  # Initialer Status des Minings

# Pfad zur XMRig-Binärdatei (anpassen, falls nötig)
xmrig_path = os.path.abspath("xmrig.exe")  # .exe für Windows

# JSON-Konfigurationsdatei
config_path = "config.json"  # Pfad zur JSON-Datei (im selben Verzeichnis)

# Funktion, um JSON-Konfiguration zu laden
def load_config(config_path):
    """
    Lädt die JSON-Konfigurationsdatei.
    :param config_path: Pfad zur JSON-Datei
    :return: Geladene Konfiguration oder None bei Fehler
    """
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Fehler beim Laden der Konfiguration: {e}")
        return None

# Funktion, um XMRig auszuführen
def run_xmrig(config):
    """
    Startet XMRig in einer Endlosschleife und überwacht den Prozess.
    :param config: Geladene JSON-Konfiguration oder None
    """
    global xmrig_logs, mining_status

    if not os.path.exists(xmrig_path):
        print(f"Fehler: XMRig wurde nicht gefunden unter {xmrig_path}.")
        return

    while True:
        print("Starte XMRig...")
        mining_status = "Active"

        try:
            if config:
                # Starte XMRig mit JSON-Konfiguration
                process = subprocess.Popen(
                    [xmrig_path],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True
                )
            else:
                # Standardargumente verwenden
                process = subprocess.Popen(
                    [
                        xmrig_path,
                        "-o", "pool.supportxmr.com:443",  # Pool-URL
                        "-u", "47SoHaddieiTiuTvczsrbvLdMMLYbk3wKjBbtag8xqErLsPwHABwCtHJiawhC7sS97WJd52KrL1cxTENHS4foTu98rHm1Gs",  # Mining-Adresse
                        "-p", "MyRig",             # Passwort (oft Standard: 'x')
                        "--cpu-priority", "3"  # CPU-Priorität (3 = niedrig)
                    ],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True
                )

            while True:
                # Lese die Prozessausgabe
                output = process.stdout.readline()
                if output == "" and process.poll() is not None:
                    print("XMRig-Prozess beendet. Neustart in 5 Sekunden...")
                    mining_status = "Inactive"
                    time.sleep(5)  # Wartezeit vor Neustart
                    break
                if output:
                    xmrig_logs.append(output.strip())
                    if len(xmrig_logs) > 100:  # Maximal 100 Zeilen speichern
                        xmrig_logs.pop(0)
                    print(output.strip())  # Ausgabe anzeigen
                time.sleep(0.1)  # Vermeidung von hoher CPU-Auslastung
        except Exception as e:
            print(f"Fehler beim Mining-Prozess: {str(e)}")
            mining_status = "Error"
            time.sleep(5)  # Wartezeit vor Neustart

# Hauptfunktion
if __name__ == "__main__":
    print("Lade Konfiguration...")

    # JSON-Konfiguration laden
    config = load_config(config_path)

    if config:
        print("JSON-Konfiguration erfolgreich geladen.")
    else:
        print("JSON-Konfiguration nicht gefunden oder fehlerhaft. Standardargumente werden verwendet.")

    # Hinweis für den Benutzer
    print("Starte XMRig Miner... Drücke Strg+C zum Beenden.")

    # XMRig in einem separaten Thread starten
    miner_thread = Thread(target=run_xmrig, args=(config,), daemon=True)
    miner_thread.start()

    # Halte das Hauptprogramm am Laufen
    try:
        while True:
            print(f"Mining-Status: {mining_status}")
            time.sleep(10)  # Aktualisiere den Status alle 10 Sekunden
    except KeyboardInterrupt:
        print("\nProgramm beendet. Miner wird gestoppt.")
