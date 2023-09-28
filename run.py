
























































































































































































































                                                                                                               "\"" + message.chat_id + "\""))
                                                                                                 out.content))
                                                                                                message.sender.id, p2)
                                                                                          str(message.sender.push_name), msg)
                                                                                         "%Y-%m-%d")
                                                                                         "%Y-%m-%d"))))
                                                                                         )))
                                                                                       p4)
                                                                                     str(date.today().strftime(
                                                                                     str(date.today().strftime(
                                                                                    "\"" + t + "\"",
                                                                                    s,str(message.sender.push_name)))
                                                                                 )))
                                                                                str(message.sender.id) == YOUR_MOBILE_NUMBER + "@c.us") or message.sender.id in driver.wapi_functions.getGroupAdmins(
                                                                               s):
                                                                             str(date.today().strftime("%Y-%m-%d")
                                                                         "Fail!!\n Number is invalid or Format for adding number is:\n#add 918888888888")
                                                                      bot_added[message.chat_id]) + out)
                                                                      message.chat_id), "")
                                                                  "Count of messages of all members\n(From {})\n\n".format(
                                                                  driver.wapi_functions.getGroupInviteLink(
                                                                 "Empty parameter! Choose a piece h or c\nExample:- #pmove c")
                                                                all_members[i])
                                                               "\"" + message.sender.id + "\"","\"" + str(message.sender.push_name) + "\""))
                                                              "https://github.com/Shyguy99/Whatsapp-bot", "")
                                                             "Empty Answer.Write your answer after #ans\nCheck current word by sending #currword")
                                                             "Empty Code!!Write some code after the command\Example:-\n#run python3#\nprint(\"Hello World\")")
                                                             "First you have to throw the dice by sending #rdice")
                                                             "Invalid command!\n Check valid command using #help_mine")
                                                             "Invalid command!\n Check valid command using #help_mine")
                                                             "The person you are trying to play with is already in a game 😐")
                                                             "Wrong input! Please check\n You have to choose two pairs Example:- #m 12 34")
                                                             "You are already in the game! 🤓\nSend #ans your answer to guess.")
                                                             "You don't have any tag left or your tags are updating\nTry later.")
                                                             "You have already threw the dice.Move your dice by sending #pmove h or #pmove c")
                                                             message.chat_id], out))
                                                         "Empty parameter!You have to choose the box using row and column\nExample:-#mine 23")
                                                         "Empty parameter!You have to choose the box\nExample:-#minemark 34")
                                                         "Getting all counts got error:\n" + str(e))
                                                         "Getting last tag got error:\n" + str(e))
                                                         "Got some error!\nCause can be:Tagged Message Deleted")
                                                         "Someone using the compiler.\nLet him/her finish or use #resetrun to terminate")
                                                         "Wrong Command 🤐!\nType #ticgame <tag the person>.")
                                                         "Wrong input! Please check\n You have to choose two pairs \nExample:- #m 12 34")
                                                         "You first have to join the game\nSend #join your name")
                                                         "{} message count from {}:\n\n*{}*".format(name, bot_added[
                                                         '*Title* :{}\n*Source* : {}\n{}'.format(out.title, out.url,
                                                         args=(Word.players[message.sender.id],)).start()
                                                     "Empty expression. Write some exp after *#calc* \nExample:- #calc 2+12")
                                                     "Empty Parameter! Type the coin symbol\nExample:- #cdetail btc")
                                                     "Empty Parameter! Type the coin symbol\nExample:- #cprice btc")
                                                     "Empty parameter!!You have give some word to be searched\nExample:-#wiki money")
                                                     "Game haven't started yet!\nSend #wordgame to start.")
                                                     "Getting msg count got error:\n" + str(e))
                                                     "Number of players must be between 2 to 4.\nCurrent number of players- {}").format(
                                                     "Starting bot for group failed" + str(e))
                                                     "Word Game already in progress 🏁\n Send #currword to check the word to be guessed.")
                                                     "You already started the game!\n Send #quitmatch to end ur game")
                                                     "You are already in a game!\nQuit it by sending #quit_tic")
                                                     "You are not in the game!\n Send #matchgame to start.")
                                                     "You don't have any match!\nType #ticgame tag the person to play with. to start the game.")
                                                     "You don't have any ongoing match!\nType #ticgame tag the person to play with to start the game.")
                                                     "You don't have any ongoing match!\nType #ticgame tag the person to play with. to start the game.")
                                                     "You have already started the game!🤐\nQuit previous game to start again")
                                                     "You have quit your game in middle!🤭\n*LOSER!!*")
                                                     "You haven't started your game yet 😅\nStart it by sending #minegame")
                                                     "You haven't started your game yet 😅\nStart it by sending #minegame")
                                                     "You haven't started your game yet 😅\nStart it by sending #minegame")
                                                     "You haven't started your game yet 😅\nStart it by sending #minegame")
                                                     "Your game haven't started yet!!\nStart it by sending #matchgame")
                                                    del ludo_game_dict[pl]
                                                driver.chat_send_message(message.chat_id,
                                                driver.chat_send_message(message.chat_id, "Can't remove")
                                                for pl in t:
                                                print("Participant added")
                                                print("Participant Removed")
                                                t = ludo_game_dict[message.sender.id].li_players[:]
                                             "Adding msg count got error:\n"+str(e))
                                             ("\"" + message.chat_id + "\"", "\"" + message.sender.id + "\""))
                                            2):
                                            driver.chat_send_message(message.chat_id, "Wrong piece!! Choose c or h")
                                            else:
                                            else:
                                            if driver.add_participant_group(message.chat_id, s):
                                            if driver.remove_participant_group(message.chat_id,
                                            if len(ludo_game_dict[message.sender.id].cur_player_list) == 0:
                                            ludo_game_dict[message.sender.id].move_piece(driver, message, s)
                                            match_player_dict[message.sender.id].diff,
                                         ("\"" + message.chat_id + "\"", "\"" + s + "\""))
                                        conn.commit()
                                        cur.execute('CALL add_player(\'{}\',\'{}\')'.format(message.sender.id, s))
                                        del match_player_dict[message.sender.id]
                                        del mine_player_dict[message.sender.id]
                                        driver.chat_send_message(message.chat_id,
                                        driver.chat_send_message(message.chat_id, "Wait! Try again")
                                        driver.wapi_functions.sendMessage(message.chat_id, "Bot not admin yet")
                                        else:
                                        else:
                                        if "#kick" in message.content:
                                        if s == "h" or s == "c":
                                        ludo_game_dict[i] = ludo_game_dict[message.sender.id]
                                        message.sender.id].status == "Won":
                                        mine_player_dict[message.sender.id].mark_pos(driver, message, s[1], 0)
                                        mine_player_dict[message.sender.id].mark_pos(driver, message, s[1], 1)
                                        p3 = fin_s[2]
                                        p4 = fin_s[3]
                                        p_adding = 0
                                        p_adding = 1
                                        s = 0
                                        s = int(s)
                                        s_adding = 0
                                        s_adding = 1
                                        threading.Thread(target=add_score,
                                        Word.enter_game(driver, message, s)
                                        Word.new_word(driver, message)
                                    'CALL add_tag_msg(\'{}\',\'{}\',\'{}\',\'{}\')'.format("\"" + message.chat_id + "\"",
                                    all_count[id] = int(getcount[j])
                                    COMP.run(driver, message, lang, code)
                                    driver.chat_send_message(message.chat_id,
                                    driver.chat_send_message(message.chat_id,
                                    driver.chat_send_message(message.chat_id,
                                    driver.chat_send_message(message.chat_id,
                                    driver.chat_send_message(message.chat_id,
                                    driver.chat_send_message(message.chat_id,
                                    driver.chat_send_message(message.chat_id,
                                    driver.chat_send_message(message.chat_id,
                                    driver.chat_send_message(message.chat_id,
                                    driver.chat_send_message(message.chat_id,
                                    driver.chat_send_message(message.chat_id, "Don't choose same pairs")
                                    driver.chat_send_message(message.chat_id, "Invalid Players")
                                    driver.chat_send_message(message.chat_id, "Name already taken!")
                                    driver.chat_send_message(message.chat_id, 'Sorry!! Admin command')
                                    driver.chat_send_message(message.chat_id, msg)
                                    else:
                                    else:
                                    else:
                                    else:
                                    else:
                                    fin_s = list(fin_s)
                                    for i in fin_s:
                                    id = getcount[i].replace("\"", "").replace("@c.us", "")
                                    if "unmark" in s[0]:
                                    if isAdmin(message.chat_id):
                                    if len(fin_s) > 2:
                                    if len(fin_s) > 3:
                                    if len(s) != 0:
                                    if len(s) == 1:
                                    if match_player_dict[message.sender.id].corr == pow(
                                    if mine_player_dict[message.sender.id].status == "Lose" or mine_player_dict[
                                    if p_adding == 0 and s_adding == 0:
                                    if Word.ans(driver, message, s):
