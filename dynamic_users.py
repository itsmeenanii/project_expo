import sqlite3
import streamlit as st

DB_NAME = "child_usage.db"

# -----------------------------
# Database initialization
# -----------------------------
def init_user_tables():
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    cur = conn.cursor()

    # Parents table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS parents (
        parent_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # Children table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS children (
        child_id INTEGER PRIMARY KEY AUTOINCREMENT,
        parent_id INTEGER,
        child_name TEXT,
        FOREIGN KEY(parent_id) REFERENCES parents(parent_id)
    )
    """)

    conn.commit()
    conn.close()


# -----------------------------
# Parent & child operations
# -----------------------------
def add_parent(username: str, password: str):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO parents (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    conn.close()


def add_child(parent_username: str, child_name: str):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        "SELECT parent_id FROM parents WHERE username=?",
        (parent_username,)
    )
    parent = cur.fetchone()

    if parent:
        cur.execute(
            "INSERT INTO children (parent_id, child_name) VALUES (?, ?)",
            (parent[0], child_name)
        )
        conn.commit()

    conn.close()


def get_children_for_parent(parent_username):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        SELECT c.child_name
        FROM children c
        JOIN parents p ON c.parent_id = p.parent_id
        WHERE p.username = ?
    """, (parent_username,))

    children = [row[0] for row in cur.fetchall()]
    conn.close()
    return children


# -----------------------------
# Authentication
# -----------------------------
def authenticate_parent(username, password):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        "SELECT parent_id FROM parents WHERE username=? AND password=?",
        (username, password)
    )
    user = cur.fetchone()
    conn.close()
    return user is not None


# -----------------------------
# Sidebar UI (used in main.py)
# -----------------------------
def parent_child_ui():
    st.subheader("👨‍👩‍👧 Parent Setup")

    with st.expander("➕ Create parent account"):
        p_user = st.text_input("New parent username")
        p_pass = st.text_input("New parent password", type="password")
        if st.button("Create Parent"):
            if p_user and p_pass:
                add_parent(p_user, p_pass)
                st.success("Parent account created")

    with st.expander("➕ Add child"):
        parent_user = st.text_input("Parent username (existing)")
        child_name = st.text_input("Child name")
        if st.button("Add Child"):
            if parent_user and child_name:
                add_child(parent_user, child_name)
                st.success("Child added successfully")
