FROM node:16-alpine

ENV APP_ROOT /app
ENV NODE_ENV production

WORKDIR ${APP_ROOT}
ADD app ${APP_ROOT}

RUN ls

RUN yarn install
RUN yarn build

CMD ["yarn", "start"]