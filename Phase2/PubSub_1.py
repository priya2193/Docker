import random

class PubSubSystem:
    publishers = {}
    subscribers = {}
    topics = {}
    topic_list = set()
    
    def register_subscribers(self,sub,t):
        if sub in self.subscribers:
            self.subscribers.setdefault(sub, [])[t] = 1
#             self.subscribers.setdefault(t, []).append(sub)   
        else:
            self.subscribers[sub] = [t]
        if t in self.topics:
            self.topics.setdefault(t, []).append(sub)
#                 self.topics.setdefault(t, [])[sub] = 1
        else:
            self.topics[t] = [sub]
#         print(self.topics)

    def register_publishers(self, pub,t):
        if pub in self.publishers:
            self.publishers.setdefault(pub, [])[t] = 1
#             self.subscribers.setdefault(t, []).append(sub)   
        else:
            self.publishers[pub] = [t]
#         self.publishers.add(pub)
        
    def add_topic(self,t):
        self.topic_list.add(t)
            
    def print_pub_sub_system(self):
        print(self.topics)
        print(self.subscribers)
        print(self.publishers)

    def receive_and_notify(self,publisher,topic):
#         print(self.topics[topic])
        for val in self.topics[topic]:
            val.notify(publisher,topic)

class Subscriber:
    def __init__(self, name):
        self.name = name
    def notify(self,publisher,topic_content):
        print('{} received "{}" from {}'.format(self.name,topic_content,publisher.name))

class Publisher:
    def __init__(self, name):
        self.name = name
        self.topics = set()
        
    def add_topic(self,t):
        self.topics.add(t)
        
    def publish(self,pub_sub_system,topic):
        pub_sub_system.receive_and_notify(self,topic)  
    
class Test:
    def subscription_generator(self, val, pub_sub_system):
        topics = ['TECHNOLOGY', 'SPORTS', 'BUSINESS', 'POLITICS', 'FASHION']
        rand_s = random.randint(0,4)
        rand = random.randint(0,4)
        pub_sub_system.add_topic(topics[rand])
        s = Subscriber('S' + str(val))
        res = 'Subscriber ' + str(s.name) + ' created and subscribed to topic '+ str(topics[rand])
        pub_sub_system.register_subscribers(s,topics[rand])
        return res

    def publisher_generator(self, val, pub_sub_system):
        topics = ['TECHNOLOGY', 'SPORTS', 'BUSINESS', 'POLITICS', 'FASHION']
        p = Publisher('p' + str(val))
        rand = random.randint(0,4)
        pub_sub_system.register_publishers(p,topics[rand])
        res = 'Publisher ' + str(p.name) + ' created for topic '+ str(topics[rand])
        return res

    def notify(self, pub_sub_system):
        topics = []
        for t in pub_sub_system.topic_list:
            topics.append(t)
        rand = random.randint(0,len(topics) - 1)
        publishers = []
        for p in pub_sub_system.publishers:
            publishers.append(p)
        rand = random.randint(0,len(topics) - 1)
        rand_p = random.randint(0,len(publishers) - 1)
        print(rand_p)
        publishers[rand_p].publish(pub_sub_system, topics[rand])

    def myMain(self):
        pub_sub_system = PubSubSystem()
        i = 1
        while(i != 10):
            res = self.subscription_generator(i, pub_sub_system)
            res_p = self.publisher_generator(i, pub_sub_system)
            i = i + 1
            print(res)
            print(res_p)
        self.notify(pub_sub_system)
