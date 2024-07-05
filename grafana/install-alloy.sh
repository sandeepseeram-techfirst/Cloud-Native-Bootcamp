# Install Alloy
sudo apt install gpg -y && \
sudo mkdir -p /etc/apt/keyrings/ && \
wget -q -O - https://apt.grafana.com/gpg.key | gpg --dearmor | sudo tee /etc/apt/keyrings/grafana.gpg > /dev/null && \
echo "deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://apt.grafana.com stable main" | sudo tee /etc/apt/sources.list.d/grafana.list && \
sudo apt-get update && \
sudo apt-get install alloy -y && \

# Modify the Alloy service configuration to listen on the desired port
sudo sed -i -e 's/CUSTOM_ARGS=""/CUSTOM_ARGS="--server.http.listen-addr=0.0.0.0:12345"/' /etc/default/alloy && \

# Enable and start the Alloy service
sudo systemctl enable alloy && \
sudo systemctl start alloy.service && \
clear && \
echo "Installation script has now been completed."