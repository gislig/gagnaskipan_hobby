class Supporters:
    def __init__(self, ticket_id = None, ticket_name = None, ticket_content = None):
        self.ticket_id = ticket_id
        self.ticket_name = ticket_name
        self.ticket_content = ticket_content

    def get_dict(self):
        return {"ticket_id":self.ticket_id,"ticket_name":self.ticket_name,"ticket_content":self.ticket_content}

class SupporterList:
    def __init__(self, Supporters = []):
        self.supporters = Supporters
        self.size = 0

    def insert(self, supporters):
        self.supporters.append(supporters)
        self.size += 1

    def query(self):
        query = """
        SELECT 
        ticket_id,
        ticket_name,
        ticket_content
        FROM tickets
        """
        return query

    def get_all(self, cursor):
        cursor.execute(self.query())
        new_supportlist = SupporterList()
        row = cursor.fetchone()
        
        while row:
            new_support = Supporters(ticket_id = row[0], ticket_name = row[1],ticket_content = row[2])
            new_supportlist.insert(new_support)
            row = cursor.fetchone()

        return new_supportlist

    def __len__(self):
        return self.size

    def __iter__(self):
        for i in range(len(self.supporters)):
            yield self.supporters[i]
