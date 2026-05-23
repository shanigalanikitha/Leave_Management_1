import streamlit as st
import requests
import pandas as pd

# -------------------------------
# Configuration
# -------------------------------
st.set_page_config(
    page_title="Leave Management System",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

BASE_URL = "http://127.0.0.1:8000"

# -------------------------------
# Sidebar Navigation
# -------------------------------
menu = ["Dashboard", "Create User", "User List", "Apply Leave", "Update Leave"]
choice = st.sidebar.selectbox("Menu", menu)

# -------------------------------
# Dashboard Page (Clean Version)
# -------------------------------
if choice == "Dashboard":
    st.markdown("<h1 style='text-align:center; color:#2C3E50;'>📊 Leave Management Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<hr style='height:3px;border:none;background-color:#4CAF50;' />", unsafe_allow_html=True)

    try:
        response = requests.get(f"{BASE_URL}/leaves/")
        if response.status_code == 200:
            leaves = response.json()
            df = pd.DataFrame(leaves)

            if not df.empty:
                chart_data = df['status'].value_counts()

                # Metrics
                col1, col2, col3 = st.columns(3)
                col1.metric("Total Leaves", len(df))
                col2.metric("Approved ✅", chart_data.get("approved", 0))
                col3.metric("Pending ⏳", chart_data.get("pending", 0))

                # Bar chart
                st.markdown("### 📈 Leave Status Overview")
                st.bar_chart(chart_data)

            else:
                st.info("No leaves applied yet.")
        else:
            st.warning("Unable to fetch data from backend.")
    except:
        st.warning("Backend not connected. Please run FastAPI server.")

# -------------------------------
# Create User Page
# -------------------------------
elif choice == "Create User":
    st.header("Create User 👤")
    with st.form("user_form"):
        name = st.text_input("Name")
        role = st.selectbox("Role", ["employee", "manager"])
        submitted = st.form_submit_button("Create User")
        if submitted:
            response = requests.post(f"{BASE_URL}/users/", json={"name": name, "role": role})
            if response.status_code == 200:
                st.success(f"User '{name}' created successfully as '{role}'")
            else:
                st.error("Failed to create user")

# -------------------------------
# User List Page with Search
# -------------------------------
elif choice == "User List":
    st.header("User List 👥")

    try:
        response = requests.get(f"{BASE_URL}/users/")
        if response.status_code == 200:
            users = response.json()

            if users:
                df = pd.DataFrame(users)

                # 🔍 Search box
                search = st.text_input("Search by Name")

                if search:
                    df = df[df["name"].str.contains(search, case=False)]

                # Show filtered data
                st.dataframe(df)

                st.success(f"Total Users: {len(df)}")

            else:
                st.info("No users found.")
        else:
            st.warning("Unable to fetch users.")
    except:
        st.warning("Backend not connected.")
# -------------------------------
# Apply Leave Page
# -------------------------------
elif choice == "Apply Leave":
    st.header("Apply Leave 📝")
    leave_reasons = [
        "Sick Leave",
        "Casual Leave",
        "Maternity Leave",
        "Paternity Leave",
        "Emergency Leave",
        "Vacation Leave",
        "Work From Home"
    ]
    with st.form("apply_leave_form"):
        col1, col2 = st.columns(2)
        with col1:
            user_id = st.number_input("User ID", min_value=1)
        with col2:
            reason = st.selectbox("Reason", leave_reasons)
        submitted = st.form_submit_button("Apply Leave")
        if submitted:
            response = requests.post(f"{BASE_URL}/leave/", json={"user_id": user_id, "reason": reason})
            if response.status_code == 200:
                st.success(f"Leave applied successfully for reason: {reason}")
            else:
                st.error("Failed to apply leave")

# -------------------------------
# Update Leave Status Page
# -------------------------------
elif choice == "Update Leave":
    st.header("Update Leave Status 🔄")
    with st.form("update_leave_form"):
        leave_id = st.number_input("Leave ID", min_value=1)
        status = st.selectbox("Status", ["pending", "approved", "rejected"])
        submitted = st.form_submit_button("Update Leave")
        if submitted:
            response = requests.put(f"{BASE_URL}/leave/{leave_id}", json={"status": status})
            if response.status_code == 200:
                st.success(f"Leave ID {leave_id} updated to '{status}'")
            else:
                st.error("Failed to update leave")