FROM mongo:latest

# Exposez le port par défaut de MongoDB
EXPOSE 27017

FROM node:14

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000
CMD ["npm", "start"]