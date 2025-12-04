FROM node:20-alpine

WORKDIR /app

COPY package.json ./

RUN npm install --legacy-peer-deps

COPY . .

RUN rm -f package-lock.json

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "--port", "5173"]