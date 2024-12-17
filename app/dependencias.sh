#!/bin/bash
# Atualiza a lista de pacotes
echo "Atualizando lista de pacotes."
sudo apt update
# Pergunta se o usuário quer continuar com a atualização completa
read -p "Deseja continuar com a atualização do sistema? (s/n): " answer
if [ "$answer" != "${answer#[Ss]}" ] ;then
echo "Realizando upgrade do sistema..."
sudo apt upgrade
else
echo "Upgrade cancelado."
fi
# Instalar dependências
echo "Instalando dependências..."
sudo apt install -y git
sudo apt install -y htop
sudo apt install -y net-tools
sudo apt install -y curl
echo "Todas as dependências foram instaladas!"