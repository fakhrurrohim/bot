                                    j += 1
                                    ludo_game_dict[message.sender.id] = karma_bot.ludo(driver, message, p1, p2, p3,
                                    ludo_game_dict[message.sender.id].dice(driver, message, s)
                                    match_player_dict[message.sender.id].guess(driver, message, s1, s2)
                                    mine_player_dict[message.sender.id] = karma_bot.mine(driver, message, int(s[1]))
                                    mine_player_dict[message.sender.id].choose(driver, message, s)
                                    msg = out
                                    out += str(value) + "--> " + str(key) + "\n"
                                    out = out[0]
                                    p1 = fin_s[0]
                                    p2 = fin_s[1]
                                    p3 = None
                                    p4 = None
                                    s = message.content.replace("#pmove", "").lower()
                                    s = message.content.replace("#rdice", "")
                                    s = s.strip()
                                    s_time = s_time + 1800
                                    tag_ids_us.add(t)
                                    tic_player_dict[message.sender.id] = karma_bot.tic_tac_game(driver, message,
                                    tic_player_dict[p2] = tic_player_dict[message.sender.id]
                                "@" + str(message.sender.id).replace("@c.us", ""),
                                "@" + str(pl[0]).replace("@c.us", ""))
                                'CALL update_ignore_list(\'{}\',\'{}\')'.format("\"" + id + "\"", 0))
                                'CALL update_ignore_list(\'{}\',\'{}\')'.format("\"" + id + "\"", 1))
                                all_parti = driver.wapi_functions.getGroupAdmins(message.chat_id)
                                all_parti = driver.wapi_functions.getGroupParticipantIDs(message.chat_id)
                                all_parti = set(driver.wapi_functions.getGroupParticipantIDs(message.chat_id))
                                break
                                break
                                code = s[idx + 1:]
                                conn.commit()
                                continue
                                cur.callproc('get_all_msg_count', ("\"" + message.chat_id + "\"",))
                                cur.callproc('get_last_tag',
                                cur.execute(
                                del ludo_game_dict[ludo_game_dict[message.sender.id].cur_player_list[0]]
                                del tic_player_dict[pl[0]]
                                del tic_player_dict[pl[1]]
                                diff = int(s[1])
                                driver.chat_send_message(message.chat_id,
                                driver.chat_send_message(message.chat_id,
                                driver.chat_send_message(message.chat_id,
                                driver.chat_send_message(message.chat_id,
                                driver.chat_send_message(message.chat_id,
                                driver.chat_send_message(message.chat_id,
                                driver.chat_send_message(message.chat_id,
                                driver.chat_send_message(message.chat_id,
                                driver.chat_send_message(message.chat_id,
                                driver.chat_send_message(message.chat_id, "Can't find anything!!")
                                driver.chat_send_message(message.chat_id, "Empty Name!!Write your name after #join.")
                                driver.chat_send_message(message.chat_id, "Fail!!")
                                driver.chat_send_message(message.chat_id, "Game ended!")
                                driver.chat_send_message(message.chat_id, "Not your chance")
                                driver.chat_send_message(message.chat_id, "Not your chance")
                                driver.chat_send_message(message.chat_id, "One or more player is already in a game.")
                                driver.chat_send_message(message.chat_id, "Only bot message can be deleted!!")
                                driver.chat_send_message(message.chat_id, "Wrong input 😐")
                                driver.chat_send_message(message.chat_id, "{} message count:\n\n*1*.".format(name))
                                driver.chat_send_message(message.chat_id, str(e))
                                driver.chat_send_message(message.chat_id, str(e))
                                driver.chat_send_message(YOUR_MOBILE_NUMBER + "@c.us",
                                driver.chat_send_message(YOUR_MOBILE_NUMBER + "@c.us",
                                driver.remove_participant_group(message.chat_id,
                                driver.wapi_functions.sendMessage(message.chat_id,
                                elif s in Word.players.values():
                                elif s1.isdigit() and s2.isdigit():
                                else:
                                else:
                                else:
                                else:
                                else:
                                else:
                                else:
                                else:
                                else:
                                else:
                                else:
                                else:
                                exec("driver.chat_send_message(message.chat_id,str({}))".format(k))
                                exec(str(message.content))
                                flag=1
                                for i in range(l):
                                for key, value in all_count.items():
                                getcount = cur.fetchone()[0]
                                i.reply_message("hello")
                                idx = s.index("#")
                                if fin_s.issubset(all_parti):
                                if len(code) > 3:
                                if len(s) > 2:
                                if ludo_game_dict[message.sender.id].dthrow == 0:
                                if ludo_game_dict[message.sender.id].dthrow == 1:
                                if message.sender.id in driver.wapi_functions.getGroupAdmins(message.chat_id):
                                if message.sender.id in Word.players.keys():
                                if message.sender.id not in mine_player_dict:
                                if out[0] == None:
                                if p2 not in tic_player_dict:
                                if s.isdigit():
                                if s.isdigit():
                                if s1 == s2:
                                if t in all_member:
                                j = l
                                l = len(getcount) // 2
                                lang = s1.replace("run ", "")
                                limit -= 1
                                match_player_dict[message.sender.id] = (karma_bot.matcher(driver, message))
                                match_player_dict[message.sender.id] = (karma_bot.matcher(driver, message, diff))
                                message.sender.id) == YOUR_MOBILE_NUMBER + "@c.us":
                                mine_player_dict[message.sender.id] = karma_bot.mine(driver, message)
                                msg += " @{} \n".format(i).replace("@c.us", "")
                                msg = msg.replace(t, "").replace('\'',"").replace("\""," ")
                                n += 1
                                name = message._js_obj["quotedMsgObj"]['sender']['pushname']
                                out = ""
                                out = cur.fetchone()
                                out = out[0]
                                out = wikipedia.page(s)
                                p2 = s[1].replace("@", "") + "@c.us"
                                pl = tic_player_dict[message.sender.id].players
                                print("Getting all counts got error:\n" + str(e))
                                print("Getting last tag got error:\n" + str(e))
                                print(f"Error -> {str(e)}")
                                print(fin_s, all_parti)
                                print(getcount)
                                s = "Tagged in a {} by {} with the message:\n\n{}".format( message.type,
                                s = message._js_obj["quotedMsgObj"]["sender"]["id"]
                                s = message._js_obj["quotedMsgObj"]['sender']['id']
                                s = message.content.replace("#ans", "")
                                s = message.content.split("#tagadmins")
                                s = message.content.split("#tagall")
                                s = message.content[1:]
                                s = s.strip()
                                s1 = s[0]
                                s1 = s[:idx].strip()
                                s2 = s[1]
                                str(len(fin_s)))
                                t = "@" + t.replace("@c.us", "")
                                t = tag_id + "@c.us"
                                tag_id = msg[i + 1:i + 13]
                                time.sleep(1)
                            "*Compiler*✅ \n-Run any language code by sending \n*#run* _language_name_# \nWrite your code here from next line\n\n-Put language name as  cpp,python3, c, java, etc\nNote-: Don't give runtime input statements or try to run infinite loop,it will give error.\n\n--------------------------------------------------\n")
                            "*Geeks for Geeks code extractor*✅\n-Get the code from geeks for geeks site according to the asked question.\n-To get the code for particular problem, type \n\n*#gfg#*_Your question_*#*_the language in which you want the code_\n\nEx-: ->*#gfg#merge sort#python*\n     ->*#gfg #kadane algorithm#c++*.\n\n--------------------------------------------------\n")
                            "*Ludo*✅ \n-Play Ludo with your friends on whatsapp. \nSend *#help_ludo* to know how to play.\n\n--------------------------------------------------\n")
                            "*Match Emoji Game*✅\n\n-To start the game send *#matchgame*\n-For setting level add 2 or 4 or 6 after *#matchgame* with a space\n-For more detail send *#help_match*.\n\n--------------------------------------------------\n")
                            "*Minesweeper Game*✅.*\n\n-To start the game send *#minegame* and to chosse a pair send *#mine* _xy_ where x is row and y is column.\n-For more commands of this game use #help_mine.\n-To know how to play visit-https://www.instructables.com/How-to-play-minesweeper/ \n\n--------------------------------------------------\n")
                            "*Some admin/extra commands*\n\n- *#delete* to delete the bot message.\n-*#add* _919876543210_\n- *#kick* _tag the person you want to remove_\n- *#link* for getting the link of the group\n- *#tagall* \n- *#tagadmins* \n-Note-: You can also add some text after #tagall and #tagadmins.\n\nBot created by *_Karma_*\nGithub link-:https://github.com/Shyguy99/Whatsapp-bot")
                            "*Tagger and Counter*✅\n\n-Now you will not miss the tags\nCheck where you were tagged by using *#last_tag* command.\n-Use it again to check second last tag and so on.\n-You can check upto last 50 tags.\n\n-You can also check the total number of messages you have sent by using *#msg_count* .\n\n--------------------------------------------------\n")
                            "*Tic Tac Toe Game*✅\n-To play send *#ticgame* _tag the number you want to play with_\n-To end the game early send *#quit_tic*\nType #help_tic for controls.\n\n--------------------------------------------------\n")
                            "*Welcome to the I-Bot*\n\n*Features*\n\n*Crypto*✅ \n-Check the price of crypto coin by sending \n*#cprice* _coin_ \n\n-Check latest crypto news by sending *#cnews* \nFor specific topic send *#cnews* _topic or coin name_\n\n-Check detail of a coin by sending *#cdetail* _coin_ .\n\n--------------------------------------------------\n")
                            "*Wikipedia Search*✅.*\n\n-Search anything on wikipedia by sending *#wiki* _title_\n\nEx. *#wiki monkey*.\n\n--------------------------------------------------\n")
                            "*Word game*✅\n-To start send #wordgame\n-Type #help_wgame for controls.\n\n--------------------------------------------------\n")
                            # check if match ended then remove the players
                            'select member_id from members_table where msg_count>{} and chat_id=\'{}\''.format(s,
                            (message.type == 'image' or message.type == 'video') and (hasattr(message, 'caption'))):
                            all_count = dict()
                            all_member = driver.wapi_functions.getGroupParticipantIDs(message.chat_id)
                            ar = [i for i, j in zip(count(), msg) if j == "@"]
                            bot_added[message.chat_id] = str(date.today().strftime("%Y-%m-%d"))
                            break
                            COMP.inuse = 0
                            conn.commit()
                            conn.commit()
                            conn.commit()
                            conn.commit()
                            continue
                            Crypto.detail(driver, message, s)
                            Crypto.price(driver, message, s)
                            cur.callproc('get_msg_count',
                            cur.execute(
                            cur.execute(
                            cur.execute('CALL add_chat(\'{}\',\'{}\',\'{}\')'.format("\"" + message.chat_id + "\"", 0,
                            cur.execute('CALL add_chat(\'{}\',\'{}\',\'{}\')'.format("\"" + message.chat_id + "\"", 1,
                            db_members = 0
                            db_members = 0
                            db_members = 1
                            db_members = 1
                            del ludo_game_dict[message.sender.id]
                            del match_player_dict[message.sender.id]
                            del mine_player_dict[message.sender.id]
                            del tic_player_dict[message.sender.id]
                            del tic_player_dict[pl[0]]
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
                            driver.chat_send_message(message.chat_id, "Admin Command!!")
                            driver.chat_send_message(message.chat_id, "Done!!")
                            driver.chat_send_message(message.chat_id, "Done!!")
                            driver.chat_send_message(message.chat_id, "Fail!!")
                            driver.chat_send_message(message.chat_id, "Game not started yet!\nSend #wordgame to start")
                            driver.chat_send_message(message.chat_id, "He is already in ignore list!")
                            driver.chat_send_message(message.chat_id, "He is not in ignore list")
                            driver.chat_send_message(message.chat_id, "I-Bot failed to start for this chat!")
                            driver.chat_send_message(message.chat_id, "I-Bot failed to start for this chat!")
                            driver.chat_send_message(message.chat_id, "I-Bot is now active ✨")
                            driver.chat_send_message(message.chat_id, "I-Bot is now inactive for this chat 🥺")
                            driver.chat_send_message(message.chat_id, "No person/number tagged!!")
                            driver.chat_send_message(message.chat_id, "No quoted message!!")
                            driver.chat_send_message(message.chat_id, "Owner command only!")
                            driver.chat_send_message(message.chat_id, "Owner command only!")
                            driver.chat_send_message(message.chat_id, "Quitted!!")
                            driver.chat_send_message(message.chat_id, "Some Error Occured")
                            driver.chat_send_message(message.chat_id, "Try again in 2 sec. Let me process last query")
                            driver.chat_send_message(message.chat_id, "You are not in the game")
                            driver.chat_send_message(message.chat_id, "You are not in the game")
                            driver.chat_send_message(message.chat_id, "You are not in the game.")
                            driver.chat_send_message(message.chat_id, "You are not in the game.")
                            driver.chat_send_message(message.chat_id, "Your game deleted!")
                            driver.chat_send_message(message.chat_id, "Your game haven't started yet!!")
                            driver.chat_send_message(message.chat_id, "Your ongoing game!\n\n" + s)
                            driver.chat_send_message(message.chat_id, 'Sorry!! Admin command only')
                            driver.chat_send_message(YOUR_MOBILE_NUMBER + "@c.us",
                            driver.chat_send_message(YOUR_MOBILE_NUMBER + "@c.us",
                            driver.send_message_with_auto_preview(message.chat_id,
                            driver.wapi_functions.sendMessageWithMentions(message.chat_id, msg, '')
                            driver.wapi_functions.sendMessageWithMentions(message.chat_id, out1, "")
                            elif len(s) == 1:
                            else:
                            else:
                            else:
                            else:
                            else:
                            else:
                            else:
                            else:
                            else:
                            else:
                            else:
                            else:
                            else:
                            else:
                            except Exception as e:
                            except Exception as e:
                            except Exception as e:
                            except Exception as e:
                            except Exception as e:
                            except:
                            executable_path=os.environ.get("CHROMEDRIVER_PATH"))
                            fin_s.append(i.replace("@", "") + "@c.us")
                            for i in all_parti:
                            for i in ar:
                            for t in tag_ids_us:
                            for t in tag_ids_us:
                            group[message.chat_id] = 0
                            group[message.chat_id] = 1
                            id = message._js_obj["quotedMsgObj"]["id"]
                            id = message._js_obj["quotedMsgObj"]["sender"]["id"]
                            id = message._js_obj["quotedMsgObj"]["sender"]["id"]
                            if "#tagadmins" in message.content:
                            if all_members[i] not in p and all_members[i] != YOUR_MOBILE_NUMBER + "@c.us":
                            if COMP.inuse != 1:
                            if i.type=='chat' and i.content=="*oo":
                            if len(ludo_game_dict[message.sender.id].cur_player_list) == 1:
                            if len(s) != 0:
                            if len(s) != 0:
                            if len(s) == 2 and "@" in s[1]:
                            if len(s) == 2 and s[1].isdigit() and int(s[1]) <= 6 and int(s[1]) > 0:
                            if len(s) == 2 and s[1].isdigit() and int(s[1]) <= 6:
                            if len(s) == 2:
                            if len(s) > 0:
                            if len(set(fin_s).intersection(set(ludo_game_dict.keys()))) == 0:
                            if limit == 0:
                            if ludo_game_dict[message.sender.id].players[message.sender.id].chance == 1:
                            if ludo_game_dict[message.sender.id].players[message.sender.id].chance == 1:
                            if message._js_obj["quotedMsgObj"]:
                            if message._js_obj["quotedMsgObj"]:
                            if message.sender.id in Word.players.keys():
                            if not driver.wapi_functions.deleteMessage(message.chat_id, id, True):
                            if out[0] == None:
                            if tic_player_dict[message.sender.id].status != "":
                            if time.time() - s_time > 3600*2:
                            ignore_list.add(message._js_obj["quotedMsgObj"]["sender"]["id"])
                            ignore_list.remove(message._js_obj["quotedMsgObj"]["sender"]["id"])
                            k = message.content.replace("#reply", "").strip()
                            karma_bot.Calculator().calc(driver, message, s)
                            limit = int(l[1])
                            limit = len(all_members)
                            ludo_game_dict[message.sender.id].current_board(driver, message)
                            ludo_game_dict[message.sender.id].quit(driver, message)
                            match_player_dict[message.sender.id].current_game(driver, message)
                            msg += s[1]
                            msg = message.caption
                            msg = message.content
                            msg = msg.replace("#", "")
                            msg = s[0] + "\n"
                            name = message.sender.push_name
                            out = cur.fetchone()
                            out1 = "Match quit by {}\n{} you won!!".format(
                            pl = tic_player_dict[message.sender.id].players
                            pl.remove(message.sender.id)
                            print("Getting msg count got error:\n" + str(e))
                            print("Starting bot for group failed" + str(e))
                            print(all_members[i], p)
                            print(e)
                            print(e)
                            print(ludo_game_dict[message.sender.id].cur_player_list)
                            print(s)
                            print(str(e))
                            s = message.content.replace("#join", "")
                            s = message.content.replace("#m", "")
                            s = message.content.replace("#mine", "")
                            s = message.content.replace("#minemark", "")
                            s = message.content.split()
                            s = message.content.split()
                            s = message.sender.id
                            s = mine_player_dict[message.sender.id].listtostring(s)
                            s = mine_player_dict[message.sender.id].mine_cov_map
                            s = s.replace("#mineunmark", "")
                            s = s.replace("@", "") + "@c.us"
                            s = s.split()
                            s = s.strip()
                            s = s.strip()
                            s = s.strip()
                            s = s.strip()
                            tag_ids_us = set()
                            threading.Thread(target=main, args=(i,)).start()
                            tic_player_dict[message.sender.id].current_match()
                            tic_player_dict[message.sender.id].mark(driver, message, str(message.content)[1])
                            try:
                            try:
                            try:
                            try:
                            try:
                            try:
                            while db_members == 1:
                            Word.current_word(driver, message)
                            Word.skip(driver, message)
                            Word.wgame_start(driver, message)
                            Word.wgame_start(driver, message)
                            Word.wgame_start(driver, message)
                        'CALL add_count(\'{}\',\'{}\',\'{}\')'.format("\"" + message.chat_id + "\"",
                        all_get_tag_msg.append(message)
                        all_members = driver.wapi_functions.getGroupParticipantIDs(message.chat_id)
                        COMP.inuse = 0
                        Crypto.mmi(driver, message)
                        Crypto.news(driver, message.chat_id, CRYPTOPANIC_API, s)
                        cur.execute(
                        db_chats = 0
                        db_chats = 1
                        db_members = 0
                        db_members = 1
                        driver.chat_send_message(message.chat_id, "All commands :\n" + out)
                        driver.chat_send_message(message.chat_id, "I-Bot is already ON for this group")
                        driver.chat_send_message(message.chat_id, "Languages supported by compiler:-\n" + s)
                        driver.chat_send_message(message.chat_id, "Limit Left: " + str(200 - int(COMP.r.usage())))
                        driver.chat_send_message(message.chat_id, "Pong!!")
                        driver.chat_send_message(message.chat_id, "Program Terminated!!")
                        driver.chat_send_message(message.chat_id, "Removing inactive members....")
                        driver.chat_send_message(message.chat_id, "{} Inactive members removed".format(n))
                        driver.chat_send_message(message.chat_id, out)
                        driver.chat_send_message(message.chat_id, s)
                        driver.chat_send_message(message.chat_id, s)
                        driver.chat_send_message(message.chat_id, s)
                        driver.chat_send_message(message.chat_id, s)
                        driver.chat_send_message(message.chat_id, s)
                        driver.send_message_with_auto_preview(message.chat_id,
