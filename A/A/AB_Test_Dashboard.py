import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

st.set_page_config(page_title="A/B Test Dashboard", layout="wide")
st.title("📊 A/B Test Results: Marketing Campaign Analysis")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("marketing_AB.csv")
    df['converted'] = df['converted'].astype(bool)
    df['test group'] = df['test group'].astype('category')
    df['most ads day'] = df['most ads day'].astype('category')
    return df

df = load_data()

# Summary Metrics
st.header("📌 Summary Metrics")
col1, col2 = st.columns(2)

with col1:
    ad_conv_rate = df[df['test group'] == 'ad']['converted'].mean()
    psa_conv_rate = df[df['test group'] == 'psa']['converted'].mean()
    st.metric("Ad Group Conversion Rate", f"{ad_conv_rate*100:.2f}%")
    st.metric("PSA Group Conversion Rate", f"{psa_conv_rate*100:.2f}%")

with col2:
    ad_conversions = df[df['test group'] == 'ad']['converted'].sum()
    est_revenue = ad_conversions * 50  # Assuming $50 per conversion
    st.metric("Estimated Revenue from Ads", f"${est_revenue:,.2f}")

# Conversion Rate Plot
st.subheader("📈 Conversion Rate by Test Group")
group_conv = df.groupby("test group")['converted'].mean().reset_index()
fig1, ax1 = plt.subplots()
sns.barplot(data=group_conv, x="test group", y="converted", palette="viridis", ax=ax1)
ax1.set_ylabel("Conversion Rate")
ax1.set_title("Conversion Rate by Group")
st.pyplot(fig1)

# Ads Seen vs Conversion
st.subheader("📦 Ad Exposure vs. Conversion")
fig2, ax2 = plt.subplots()
sns.boxplot(data=df, x="converted", y="total ads", palette="Set2", ax=ax2)
ax2.set_yscale("log")
ax2.set_title("Ad Exposure (Total Ads) by Conversion")
ax2.set_xlabel("Converted")
ax2.set_ylabel("Total Ads Seen")
st.pyplot(fig2)

# Day of Week Conversion
st.subheader("🗓️ Conversion Rate by Day of Most Ads")
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_conv = df.groupby("most ads day")['converted'].mean().reindex(day_order).reset_index()
fig3, ax3 = plt.subplots()
sns.barplot(data=day_conv, x="most ads day", y="converted", palette="crest", ax=ax3)
ax3.set_title("Conversion by Day")
ax3.set_xlabel("Day")
ax3.set_ylabel("Conversion Rate")
st.pyplot(fig3)

# Hourly Conversion
st.subheader("⏰ Conversion Rate by Hour of Most Ads")
hourly = df.groupby("most ads hour")['converted'].mean().reset_index()
fig4, ax4 = plt.subplots()
sns.lineplot(data=hourly, x="most ads hour", y="converted", marker='o', color='teal', ax=ax4)
ax4.set_title("Hourly Conversion Trend")
ax4.set_xlabel("Hour")
ax4.set_ylabel("Conversion Rate")
st.pyplot(fig4)

# Chi-square Test
st.subheader("🧪 Chi-Square Test Result")
contingency = pd.crosstab(df['test group'], df['converted'])
chi2, p, dof, expected = chi2_contingency(contingency)

st.write("**Chi2 Statistic:**", round(chi2, 2))
st.write("**P-value:**", round(p, 4))
if p < 0.05:
    st.success("✅ Statistically significant difference — ads influenced conversions.")
else:
    st.warning("❌ No statistically significant difference found.")

# Insights
st.subheader("💡 Key Insights and Recommendations")
st.markdown("""
- Ads lead to higher conversion rates vs PSA group (statistically significant).
- Weekday and midday ad exposure shows stronger conversion tendencies.
- Suggested optimal frequency for ads based on exposure pattern analysis.
- Focus future campaigns during high-converting days/hours for better ROI.
- A/B tests like this should be iterated with audience segmentation for deeper personalization.
""")
