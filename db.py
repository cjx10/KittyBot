import sqlite3
import hashlib

def cursor():
    return conn.cursor()

def commit():
    conn.commit()

def start():
    c = cursor()
    c.execute("CREATE TABLE IF NOT EXISTS emoji_counts (user TEXT, emoji TEXT, count INTEGER)");
    c.execute("CREATE UNIQUE INDEX IF NOT EXISTS emoji_counts_idx ON emoji_counts (user, emoji)");
    c.execute("CREATE TABLE IF NOT EXISTS message_counts (user TEXT, count INTEGER)");
    c.execute("CREATE UNIQUE INDEX IF NOT EXISTS message_counts_idx ON message_counts (user)");
    c.execute("CREATE TABLE IF NOT EXISTS message_hashes (user TEXT, message_id TEXT, message_hash TEXT)");
    c.execute("CREATE UNIQUE INDEX IF NOT EXISTS message_hashes_idx ON message_hashes (message_hash)");
    c.execute("CREATE TABLE IF NOT EXISTS message_deletes (user TEXT, count INTEGER)");
    c.execute("CREATE UNIQUE INDEX IF NOT EXISTS message_deletes_idx ON message_deletes (user)");

def md5sum(m):
    return hashlib.md5(m.encode('utf-8')).hexdigest()

conn = sqlite3.connect('persist.sqlite')
conn.create_function("md5", 1, md5sum)
start()
