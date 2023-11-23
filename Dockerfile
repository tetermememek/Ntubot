######## Kynan #######

FROM mymasky/masky3:main


COPY installer.sh .

RUN bash installer.sh

# changing workdir
WORKDIR "/root/mymasky"

# start the bot.
CMD ["bash", "start"]
