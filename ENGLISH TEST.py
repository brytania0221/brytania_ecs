print()
print()
name = input("Enter your name? ")
while len(name) == 0:
    name = input("Please enter your name?: ")
print()
print("Hello " + " " + name + ",")

print("Welcome to English & Computer Science classroom! ")
print()
print("My name is Mr.Haris," + " " + "I am glad you are here to learn English and test your level.")
print("All of these questions had been made randomly from pre-intermediate to intermediate level." + "The correct answers are included," + " " + "There for you will be able to learn from the mistakes," + " " + "read again your English books and try again.")
print()
print("Good luck on your test!")
print()
ready = input("Hit Enter if you ready to take the test! ")


while True:
    questions = ("Please choose the correct preposition to complete this phrase:" + " " + "LABSCHOOL - Tangerang Raya Vocational School is located ________ Jl.Raya Kampung Melayu-Soekarno Hatta airport KM4." + " " + "Teluknaga - Tangerang," + " " + "BANTEN.",
                 "Please choose the correct preposition to complete this phrase:" + " " + "I was born in Bandung," + " " + "but I live ______ Tangerang now.",
                 "Please choose the correct preposition to complete this phrase:" + " " + "We are going to have mathmatic exam ____ Monday.",
                 "Please choose the correct preposition to complete this phrase:" + " " + "____ 1945," + "Indonesia's first president 'Soekarno' had proclamed the independence day of the country, 'The Republic Of Indonesia'.",
                 "Pleasa choose the correct verb tense to complete this phrase:" + " " + "My mother was cooking in the kitchen when aunt Emilia ______.",
                 "Which one is the correct form of 'Present Perfect Tense'? ",
                 "Which one is the correct form of 'Present Perfect Continouse Tense'? ",
                 "Which one is the correct form of 'Past Perfect Tense'? ",
                 "Which one is the correct form of 'Past Perfect Continous Tense'? ",
                 "Please choose the correct verb tense;" + " " + "My father was watching TV When I ______ home.",
                 "Please choose the correct verb to be;" + " " + "My friend and I ______ going to watch movie after school.",
                 "My teacher told me that I _________ study hard if I want to pass the exam.",
                 "School's cleanliness is important aspect and it's our responsibility as a student to keep our school cleans," + " " + "_________ we have schedule to clean the school.",
                 "I am drawing a grafitti and I want to apply it ____ my bedroom wall.",
                 "Asking and giving opinions are indispensable in ______ lives.",
                 "Art education can improve student's creativity." + " " + "_________ of teaching rigid formula or memorization of things," + " " + "art education uses imagination as the main aspect of education. ",
                 "The combination ________ excitement and thinking out of the box can result in creativity.",
                 "___ Art," + " " + "We decide what we want to make." + " " + "from the style to to the color preference.",
                 "He often ______ his time to see the art exhibition. ",
                 "We all know that excercise is important in _____ lives. ",
                 "Ihsan was a little bit nervouse because he hasn't _______ the song for a long time.",
                 "Bruce Willis has ___________ many famous holywood's action movies.",
                 "_____ reading," + " " + "we can get a lot of information about many things such as science," + " " + "technology," + " " + "sports," + " " + "arts and culture.",
                 "It is 'obvious' that everyone needs to read books," + " " + "online or ofline news media or others." + " " + "What is the synonym from the word 'obvious'? ",
                 "Do you know what is the relationship __________ money and corruption? ",
                 "We have to 'prevent' the young generations from getting a bad mentality of corruption." + " " + "What is the synonym from the word 'prevent'? ",
                 "Lerning English ________ music and songs can be very enjoyable.",
                 "Tourism is now very 'huge' contribution to the economies of most countries." + " " + "What is the synonym from the word 'huge'? ",
                 "River waste is very disturbing." + " " + "People do not allowed for ________ the garbage in the river.",
                 "The highest annual inflation rate in July 'occured' in the housing group and food." + " " + "What is the synonym from the word 'occured'? ",
                 "Paulina was a former princess," + " " + "Her father had _______ on his throne and became a carpenter.",
                 "_______ her father was new to the world of carpentry," + " " + "his works didn't sell as good expectation.",
                 "Which one is the correct 'negative' form," + " " + "from the phrase 'She will be wearing sunglasses when she come'? ",
                 "Which one is the correct form of 'offering' expression? ",
                 "Which one is the correct form of 'possibility' expression? ",
                 "Which one is the correct form of 'obligation' expression? ",
                 "Which one is the correct form of 'permission' expression? ",
                 "If she _______ enough money," + " " + "She would have gone to Mecca.",
                 "If he ________ the number," + " " + "he will probably make a phone call. ",
                 "She said that she _______ to sell her old car. ",
                 "If you don't get enough sleep at night." + " " + "You ____ be sleepy during the day. ",
                 "'I am going to finish my homework after dinner', " + "said Rasya." +" " + "What is the correct 'indirect speech'" + "form? ",
                 "She said, " + "'I really like chocolate.'" + " " + "What is the correct 'indirect speech' form? ",
                 "The bus has not arrived yet," + " " + "We will be late for the show." + " " + "_______ we go now? ",
                 "Adult moslems," + " " + "They do fasting ________ ramadhan.",
                 "Would you mind ________ the window?" + " " + "It's raining outside.",
                 "I couldn't turn on the wifi," + " " + "It ______ because the adaptor needs to be replaced.",
                 "Dr.Mohammad Hatta was the first vice president of Indonesia." + " " + "He was born in Bukit Tinggi on August 12th," + " " + "1902." + " " + "________" + "he still in junior high school," + " " + "he became interested in politics and join 'The League of Young Sumatran.",
                 "_________ of the construction project," + " " + "The public library will be temporary closed.",
                 "We need to share our feelings and pain with other people who care for ______.",
                 "Hamish Daud Wylie was born in Gosford-Australia but he has been ________ in Bali since 2010. ",
                 "Aminah was born in Semarang and moved to Jakarta with her parent _____ September, year 2012. ",
                 "Please choose the correct preposition:" + " " + "We are going to have English exam ____ Wednesday. ",
                 "Please choose the correct preposition:" + " " + "We go to school ______ Monday ____ Fiday. ",
                 "Please choose the correct verb tense:" + " " + "My mother was _______ in the kitchen when aunt Tina came.",
                 "Which one is the correct form of 'Present Perfect Tense'? ",
                 "Which one is the correct form of 'Present Perfect Continouse Tense'? ",
                 "Which one is the correct form of 'Past Perfect Tense'? ",
                 "Which one is the correct form of 'Past Perfect Continous Tense'? ",
                 "Environment awareness is _____ an understanding of the environment," + " " + "the inpacts of human behaviors and the infortant of its protection.",
                 "My friend and I ______ going to watch movie after school.",
                 "Digital wallet is a virtual account _______ stored our online payment transactions.",
                 "School's cleanliness is important aspect and it's our responsibility as a student to keep our school cleans," + " " + "_________ we have schedule to clean the school.",
                 "'It's going to rain,'" + " " + "they said." + " " + "Which one is the correct'Indirect Speech'form from this phrase? ",
                 "Asking and giving opinions are indispensable in ______ lives.",
                 "Art education can improve student's creativity." + " " + "_________ of teaching rigid formula or memorization of things," + " " + "art education uses imagination as the main aspect of education. ",
                 "The combination ________ excitement and thinking out of the box can result in creativity.",
                 "______ Art," + " " + "We decide what we want to make." + " " + "from the style to to the color preference.",
                 "He often ________ his time to see the art exhibition. ",
                 "Putri was a little bit nervouse on her shows because she hasn't _______ the song for a long time.",
                 "It was a good meal," + " " + "_____________?" + " " + "Which one is the correct'question tag' form of this phrase?",
                 "_____ reading," + " " + "we can get a lot of information about many things such as science," + " " + "technology," + " " + "sports," + " " + "arts and culture.",
                 "It is 'obvious' that everyone needs to read books," + " " + "online or ofline news media or others." + " " + "What is the synonym from the word 'obvious'? ",
                 "They have been living here in Tangerang ______ 2010.",
                 "She ______ to the store when it started raining.",
                 "They were _______ dinner when the guests arrived.",
                 "The weather was cold" + " " + "____ I forgot my jacket,",
                 "We ______ our friends for dinner yesterday. ",
                 "What is the correct form of the verb: " + " " + "She _____ never been to Singapore. ",
                 "Choose the correct preposition: " + " " + "I am looking forward ______ the weekend. ",
                 "Choose the correct article:" + " " + "I saw ______ interesting movie last night. ",
                 "Last saturday," + " " + "Sarah and her friends decided to spend the day _____ the beach. ",
                 "As they arrived," + " " + "The children was ran towards the water and play ____ the waves. ",
                 "I was _______ to print something when the electric power off. ",
                 "If I have a computer," + " " + "It _______ be easier for me to do my tasks.",
                 "If I ______ money on the sidewalk," + " " + "I would look for the person who dropped it.",
                 "He asked me whether he _______ borrowed my motorcycle to go to the concert.",
                 "We have to 'prevent' the young generations from getting a bad mentality of corruption." + " " + "What is the synonym from the word 'prevent'? ",
                 "Tourism is now very 'huge' contribution to the economies of most countries." + " " + "What is the synonym from the word 'huge'? ",
                 "If you don't get enough sleep at night." + " " + "You ____ be sleepy during the day. ",
                 "'I am going to finish my homework after dinner,' " + " " + "said Andika." +" " + "What is the correct 'indirect speech'" + "form? ",
                 "She said," + " " + "'I really like chocolate.'" + " " + "What is the correct 'indirect speech' form? ",
                 "_________ of the construction project," + " " + "The public library will be temporary closed.",
                 "We need to share our feelings and pain with other people who care for ______.",
                 "Which one is the correct 'adverb' as the convertion from the word 'slow'? ",
                 "Which one is the correct superlative adjective from the word 'hard' ? ",
                 "Which one is the correct 'adjective' as the convertion from the word 'create'? ",
                 "If the school environment is clean," + " " + "Students ______ comfortable in learning.",
                 "____________ of missing the opportunity to see the artist," + " " + "Some people willing to come ahead of time.",
                 "If the school environment is clean," + " " + "Students ______ comfortable in learning.",
                 "Please completed the sentence with correct form of present perfect tense. " + " " + "The teacher wasn't look happy because the students _________ finished their homeworks. ",
                 "Please completed the sentence with correct form of present perfect continous tense. " + " " + "They __________ the bathroom and it looks so dirty. ",
                 "Please completed the sentence with correct form of past perfect tense. " + " " +"He ____________ his report and sent it to the manager last week. ",
                 "Please completed the sentence with correct form of Past Continous Tense. " +" " + "It was fun." + " " + "Students __________________on the bus all the way back from summer camp last month. ",
                 "If you sick, " + "you ------- " + "see the doctor. ",
                 "If they _____ enough time, They would come to visit us. ",
                 "If she really love him, she ________ marry him. ",
                 "Ladies and gentlemen " + "," + "________you please have a sit now and enjoy the dinner. ",
                 "Excuse me," + " " + "______ I get you something to drink? ",
                 "I ________ run fast when I was seven years old but now I run a little slower. ",
                 "It's so hot today and it will be ________ in August. ",
                 "She said that she _______ to sell her old car. ",
                 "If you don't get enough sleep at night." + " " + "You ____ be sleepy during the day. ",
                 "'I am going to finish my homework after dinner', " + "said Rizki." +" " + "What is the correct 'indirect speech'" + "form? ",
                 "She said, " + "'I really like chocolate.'" + " " + "What is the correct 'indirect speech' form? ",
                 "The bus has not arrived yet," + " " + "We will be late for the show." + " " + "_______ we go now? ",
                 "Angel," + "" + "my classmate." + " " +"she often ______ for dancing class on sunday.",
                 "I prefer mineral water than soda." + " " + "Mineral water is good for ______ bodies,",
                 "My mother was cooking in the kitchen when aunt Sarah _______.",
                 "Uncle James __________ come to our house for playing chess with my father.",
                 "If I _______ you," + " " + "I would report to the police and let them take him to the jail.",
                 "The thief was trying to break the window when our neighbors ________ him. ",
                 "I used to take the bus when I ________ in Jakarta but there is no bus here in the village.",
                 "I was riding motorcycle when the accident _________." + "The truck driver was sleepy," + "lost control" + "and hit the car.",
                 "Adult moslems," + " " + "They do fasting ________ ramadhan.",
                 "Would you mind ________ the window?" + " " + "It's raining outside.",
                 "I couldn't turn on the wifi," + " " + "It ______ because the adaptor needs to be replaced.",
                 "Dr.Mohammad Hatta was the first vice president of Indonesia." + " " + "He was born in Bukit Tinggi on August 12th," + " " + "1902." + " " + "________" + "he still in junior high school," + " " + "he became interested in politics and join 'The League of Young Sumatran.",
                 "Charles Robert Darwin was born in Shrewsburry," + " " + "Engand." + " " + "He studied medicine and theology in University of Cambridge and ________ in 1831.",
                 "__________ of the construction project," + " " + "The public library will be temporary closed.",
                 "A presentation report is ___________ for a clear purpose and to a particular audience.",
                 "Which one is the correct expression of 'offering'? ",
                 "Which one is the correct expression of 'obligation'? ",
                 "Which one is the correct expression of 'permission'? ",
                 "Which one is the correct expression of 'possibility'? ",
                 "Do you mind if I ________ the office early today? ",
                 "The sun dipped below the horizon," + " " + "casting a warm golden glow ---------- the tranquil beach.",
                 "'I am studying for the test,'" + " " + "He told us." + " " + "What is the correct 'indirect speech' form? ",
                 "In recent years," + " " + "Brazil has greatly ____________ its Gross National Product because of several factors. ",
                 "You didn't go to Giant supermarket yesterday, _______________? ",
                 "If she had money," + " " + "She would have ________ to Mecca with her sister. ",
                 "Have you ever __________ the radio and TV at the same time? ",
                 "I never ______ to New York," + " " + "I hope I will visit New York someday. ",
                 "She still riding motorcycle __________ she doesn't have the license. ",
                 "Hurry up!" + " " + "They must ____________ for us.",
                 "Please meet my sister at the airport," + " " + "She will be __________ blue jeans, white shirt and red jacket.",
                 "____________ my achievements as a student and an athlete," + " " + "I have proven that I am passionate about the things I do.",
                 "All drivers _________ stop when the traffics lights on red. ",
                 "Democracy is a slow process of stumbling to the right decision _______ of going forward to the wrong one.")


    options = (("A. on", "B. at", "C. in", "D. by"),
               ("A. on", "B. at", "C. in", "D. by"),
               ("A. on", "B. at", "C. in", "D. by"),
               ("A. on", "B. at", "C. in", "D. by"),
               ("A. come", "B. came", "C. comes", "D. coming"),
               ("A. I have sent the letter", "B. I am sending the letter", "C. I was sending the letter", "D. I have been sending the letter"),
               ("A. She has returned the book", "B. She is returning the book", "C. She was returning the book", "D. She has been retuning the book"),
               ("A. They had cleaned the classroom", "B. They have cleaned the classroom", "C. They are cleaning the classroom ", "D. They had been cleaning the classroom"),
               ("A. We have finished the homework", "B. We had been finishing the homework", "C. We are finishing the homework", "D. We had finished the homework"),
               ("A. get", "B. got", "C. gotten", "D. getting"),
               ("A. is ", "B. am", "C. are", "D. was"),
               ("A. am", "B. have", "C. must", "D. shouldn't"),
               ("A. although", "B. beside", "C. there for", "D. further"),
               ("A. on", "B. at", "C. in", "D. by"),
               ("A. my", "B. your", "C. yours", "D. our"),
               ("A. although", "B. beside", "C. instead", "D. therefor"),
               ("A. between", "B. among", "C. behalf", "D. from"),
               ("A. on", "B. at", "C. in", "D. by"),
               ("A. spending", "B. spend", "C. spends", "D. spent"),
               ("A. my", "B. your", "C. yours", "D. our"),
               ("A. singing", "B. sing", "C. sang", "D. sung"),
               ("A. produced", "B. created", "C. invented", "D. makes"),
               ("A. Through", "B. Because", "C. With", "D. In"),
               ("A. obstacle", "B. curious", "C. clearly", "D. simply"),
               ("A. in", "B. from", "C. between", "D. among"),
               ("A. avoid", "B. prepare", "C. hold", "D. advance"),
               ("A. through", "B. with", "C. between", "D. by"),
               ("A. important", "B. wider", "C. higher", "D. large"),
               ("A. throw", "B. throwing", "C. threw", "D. threwing"),
               ("A. because", "B. happend", "C. become", "D. between"),
               ("A. give up", "B. gived up", "C. giving up", "D. given up"),
               ("A. since", "B. before", "C. after", "D. if"),
               ("A. She wasn't wearing sunglasses whem she come", "B. She doesn't wearing sunglasses when she come", "C. She will not be wearing sunglasses when she come", "D. She won't wearing sunglasses when she come "),
               ("A. Excuse me," + " " + "Can I go now?", "B. Would you like something?", "C. You should come on time", "D. I can do it "),
               ("A. I can help you if you want?", "B. I may not be able to do it alone", "C. She can go with you", "D. He will come sooner or later"),
               ("A. She has to go to the doctor", "B. I am going to school", "C. I will finish it later", "D. He is studying English" ),
               ("A. Can I come later?", "B. Can I get you some water?", "C. Can I help you?", "D. I can do it by myself."),
               ("A. have", "B. has", "C. had", "D. own"),
               ("A. have", "B. has", "C. had", "D. own"),
               ("A. want", "B. wants", "C. wanted", "D. won't"),
               ("A. will", "B. would", "C. can", "D. could"),
               ("A. Rasya said that he is going to finish his homework after dinner", "B. Rasya said that he was going to finish my homework after dinner", "C. Rasya said that he was going to finish his homework after dinner", "D. Rasya said that he is going to finish my homework after dinner"),
               ("A. She said that she really likes chocolate", "B. She said that she really likes chocolate", "C. She said that she really liked chocolate", "D. She said that I liked chocolate"),
               ("A. shall", "B. let's", "C. will", "D. would" ),
               ("A. during", "B. before", "C. at", "D. among"),
               ("A. closing", "B. close", "to close", "D. for closing" ),
               ("A. can", "B. could ", "C. may", "D. might"),
               ("A. when", "B. while", "C. which", "D. where"),
               ("A. Regards", "B. Beside", "C. Despite", "D. Because"),
               ("A. you", "B. them", "C. me", "D. us"),
               ("A. live", "B. lives", "C. living", "D. lived"),
               ("A. on", "B. at", "C. in", "D. by"),
               ("A. on", "B. at", "C. in", "D. by"),
               ("A. from/to", "B. from/until", "C. on/on", "D. from/with"),
               ("A. cook", "B. cooked", "C. cooks", "D. cooking"),
               ("A. I have writen the answer", "B. I am writing the answer", "C. I was writing the answer", "D. I have been writing the letter"),
               ("A. She has moved the chair", "B. She is moving the chair", "C. She was moving the chair", "D. She has been moving the chair"),
               ("A. They had cleaned the classroom", "B. They have cleaned the classroom", "C. They are cleaning the classroom ", "D. They had been cleaning the classroom"),
               ("A. We have painted the table", "B. We had been painting the table", "C. We are painting the table", "D. We had painted the table."),
               ("A. have", "B. having", "C. has", "D. had"),
               ("A. were ", "B. am", "C. are", "D. was"),
               ("A. where", "B. when", "C. which", "D. whom"),
               ("A. although", "B. beside", "C. therefor", "D. which"),
               ("A. They said that it was going to rain", "B. They said that it was raining", "C. They said it were raining", "D. They said it was raing. "),
               ("A. my", "B. your", "C. yours", "D. our"),
               ("A. although", "B. beside", "C. instead", "D. therefor"),
               ("A. between", "B. among", "C. behalf", "D. from"),
               ("A. on", "B. at", "C. in", "D. by"),
               ("A. spending", "B. spend", "C. spent", "D. spends"),
               ("A. sing", "B. sang", "C. sung", "D. singing"),
               ("A. was it?", "B. is it?", "C. wasn't it?", "D. does it?"),
               ("A. Through", "B. Because", "C. With", "D. In"),
               ("A. obstacle", "B. curious", "C. clearly", "D. simply"),
               ("A. on", "B. at", "C. in", "D. since"),
               ("A. go", "B. went", "C. gone", "D. goes"),
               ("A. having", "B. have", "C. had", "D. has"),
               ("A. because", "B. and", "C. then", "D. so"),
               ("A. meet", "B. met", "C. meeting", "D. have to meet"),
               ("A. have", "B. had", "C. has", "D. hasn't"),
               ("A. on", "B. at", "C. in", "D. for"),
               ("A. the", "B. a", "C. an", "C. some" ),
               ("A. on", "B. at", "C. in", "D. by"),
               ("A. on", "B. at", "C. in", "D. by"),
               ("A. try", "B. tried", "C. trying", "D. been tried "),
               ("A. shall", "B. might", "C. will", "D. would" ),
               ("A. find", "B. found", "C. finds", "D. was found"),
               ("A. can", "B. can't ", "C. could", "D. could't"),
               ("A. invent", "B. prepare", "C. avoid", "D. involved"),
               ("A. important", "B. famous", "C. large", "D. wide"),
               ("A. will", "B. would", "C. can", "D. could"),
               ("A. Andika said that he is going to finish his homework after dinner", "B. Andika said that he was going to finish my homework after dinner", "C. Andika said that he was going to finish his homework after dinner", "D. Andika said that he is going to finish my homework after dinner"),
               ("A. She said that she really likes chocolate", "B. She said that she really likes chocolate", "C. She said that she really liked chocolate", "D. She said that I liked chocolate"),
               ("A. Beside", "B. Because", "C. Instead", "D. Despite" ),
               ("A. you", "B. them", "C. us", "D. our"),
               ("A. slowed", "B. slowly", "C. slower", "D. slowest"),
               ("A. hardly", "B. Hardest", "C. harder", "D. Hardly ever"),
               ("A. creative", "B. creation", "C. creativity", "D. creator"),
               ("A. will", "B. will have", "C. would", "D. would have"),
               ("A. beside", "B. despite", "C. although", "D. in case"),
               ("A. will", "B. will have", "C. would", "D. would have"),
               ("A. have", "B. haven't", "C. had", "D. hadn't"),
               ("A. been cleaned", "B. have cleaning", "C. haven't been cleaning", "D. had been cleaned"),
               ("A. had finished", "B. has finished", "C. hasn't finished", "D. had finish"),
               ("A. had been singing", "B. has been singing", "C. have been singing", "D. were singing"),
               ("A. shall", "B. will", "C. should", "D. could"),
               ("A. have", "B. had", "C. get", "D. can have"),
               ("A. shall", "B. will", "C. should", "D. could"),
               ("A. shall", "B. should", "C. will", "D. would"),
               ("A. May", "B. Might", "C. would", "D. could"),
               ("A. can", "B. could", "C. will", "D. would"),
               ("A. hoter", "B. hotest", "C. heat", "D. more hot"),
               ("A. went", "B. want", "C. wants", "D. wanted"),
               ("A. can", "B. could", "C. will", "D. would"),
               ("A. Rizki said that" + " "+ "he is going to finish my homework after dinner.", "B. Rizki said that he was going to finish his homework after dinner.", "C. Rizki said that he would finish his homework after dinner.", "D. Rizki said that he will be finishing his homework after dinner."),
               ("A. She said that she really liked chocolate", "B. She said that she really likes chocolate", "C. She said that I like chocolate", "D. She said that she really wants chocolate"),
               ("A. shall", "B. may", "C. will", "D. would"),
               ("A. go", "B. went", "C. goes", "D. gone"),
               ("A. my", "B. mine", "C. your", "D. our"),
               ("A. come", "B. came", "C. comes", "D. coming"),
               ("A. use to", "B. used to", "C. uses to", "D. used"),
               ("A. was", "B. were", "C. am", "D. is"),
               ("A. catch", "B. catches", "C. catched", "D. caught"),
               ("A. was", "B. were", "C. am", "D. go to"),
               ("A. happend", "B. happens", "C. heaven", "D. happened"),
               ("A. since", "B. in", "C. during", "D. on"),
               ("A. closing", "B. close", "C. to close", "D. closed"),
               ("A. may", "B. might", "C. from", "D. could"),
               ("A. since", "B. beside", "C. when", "D. while"),
               ("A. graduate", "B. graduates", "C. graduated", "D. graduation"),
               ("A. Because", "B. In order", "C. Under", "A. The reason" ),
               ("A. write", "B. wrote", "C. writes", "D. written"),
               ("A. Can I get you something?", "B. May God bless us", "C. Can you help me?", "D. Can you give me some?"),
               ("A. I can do it", "B. I have to return the book.", "C. I may be back in an hour", "D. She will be here sooner or later."),
               ("A. May I help you?", "B. I can run faster", "C. She needs help", "D. May I come back later?"),
               ("A. I can do it", "B. I have to return the book", "C. I might be back in an hour", "D. She will be here sooner or later."),
               ("A. leave", "B. leaving", "C. leaves", "D. left"),
               ("A. across", "B. under", "C. on", "D.beyond"),
               ("A. He told us that he was studying for the test", "B. He told us that he is studying for the test", "C. He told us that he has studied for the test", "D. He told us that he has been studying for the test"),
               ("A. increase", "B. increases", "C. increased", "D. increasing" ),
               ("A. Do you?", "B. Don't you?", "C. Didn't you?", "D. Did you? "),
               ("A. go", "B. went", "C. goes", "D. gone"),
               ("A. turn on", "B. turned on", "C. turning on", "D. turns on"),
               ("A. go", "B. went", "C. gone", "D. going"),
               ("A. beside", "B. although", "C. but", "D. and"),
               ("A. be wait", "B. wait", "C. have been waiting", "D. have waited"),
               ("A. wear", "B. wears", "C. wearing", "D. wore"),
               ("A. Through", "B. beside", "C. Instead", "D. although"),
               ("A. shall", "B. should", "C. must", "D. ought to"),
               ("A. through", "B. beside", "C. although", "D. instead"))

    answers = ("A", "C", "A", "C", "B", "A", "D", "A", "B", "B", "C", "C", "C", "A", "D", "C", "A", "C", "C", "D", "D", "A", "A", "C", "C", "A", "A", "D", "B", "B", "D", "A", "C", "B", "B", "A", "A", "C", "B", "C", "A", "C", "C", "A", "A", "A", "D", "B", "D", "D" , "C", "C", "A", "A", "D", "A", "D", "A", "B", "B", "C", "C", "C", "A", "D", "C", "A", "C", "D", "C", "C", "A", "C", "D", "B", "A", "B", "B", "C", "D", "C", "B", "C", "C", "C", "B", "C", "C", "C", "A", "C", "C", "B", "C", "B", "B", "A", "A", "D" , "A", "B", "C", "A", "A", "C", "B", "B", "D", "A", "B", "D", "D", "C", "B", "A", "A", "C", "D", "B", "B", "B", "D", "A", "D", "C", "A", "B", "D", "C", "A", "D", "A", "B", "D", "C", "A", "A", "A", "C", "D", "D", "B", "A", "B", "C", "C", "A", "C", "D")
    guesses = []
    score = 0
    question_num = 0

    for question in questions:
        print("========================================================================================")
        print(question)
        for option in options[question_num]:
            print(option)
        guess = input("Enter your answer: ").upper()
        guesses.append(guess)
        while len(guess) == 0:
            guess = input("Please enter your answer: ")
        if guess == answers[question_num]:
            score += 1
            print("Your answer is:" + " " + "CORRECT!" + "," + "Jawaban anda 'BENAR'" + " " + "Thumb up!")
        else:
            print("Your answer is:" + " " + "INCORRECT!" + "," + "Jawaban anda 'SALAH'" + " " + "Belajar lagi!")
            print(f"{answers[question_num]} is the correct answer. ")

        question_num += 1

    print("----------------------------------------------")
    print("RESULTS")
    print("----------------------------------------------")

    print("answers: ", end="")
    for answer in answers:
        print(answer, end="")
    print()

    print("guesses: ", end="")
    for guess in guesses:
        print(guess, end="")
    print()

    score = int(score / len(questions) * 100)
    print("----------------------------------------------")
    print(f"Your score is: {score}%")
    print("------------------------------")

    print = input("Are you satisfied with the score? (YES/NO) :").upper()
    print = input("Do you find this exercises helpful? (YES/NO) :").upper()

    try_again = input("Do you want to try again? (YES/NO) :").upper()

    if try_again != "yes":
        break

print("Goodbye! ")
