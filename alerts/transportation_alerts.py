def generate_alerts(df):
    alerts = []
    if len(df) > 100:
        alerts.append("High traffic volume")

    if df["fare"].max() > 90000:
        alerts.append("high fare detected")

    return alerts