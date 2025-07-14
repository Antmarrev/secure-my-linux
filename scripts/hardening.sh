#!/bin/bash
# hardening.sh - Instalador de configuración segura para Linux
# Autor: Antonio Martín

echo "[INFO] Script hardening.sh inicializado. Funcionalidades en desarrollo."
📄 orchestrator.py

LOG_FILE="/var/log/hardening_script.log"

#Función para registrar el log
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a $LOG_FILE
}

# Función para actualizar el sistema
update_system() {
    log "Iniciando actualización del sistema..."
    apt update >> $LOG_FILE 2>&1
    if [ $? -eq 0 ]; then
        apt upgrade -y >> $LOG_FILE 2>&1
        if [ $? -eq 0 ]; then
            log "Sistema actualizado correctamente."
        else
            log "Error al actualizar los paquetes."
        fi
    else
        log "Error al ejecutar apt update."
    fi
}

# Llamada al script con parámetros
case "$1" in
    update)
        update_system
        ;;
    *)
        echo "Uso: $0 {update}"
        exit 1
        ;;
esac