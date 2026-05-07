import numpy as np

def normalized_array(data):
    """
    מנרמלת מערך נתונים לטווח של [0, 1] לפי שיטת Min-Max Scaling.
    
    הנוסחה לביצוע:
    x_norm = (x - min) / (max - min)
    
    פרמטרים:
    data (list or np.array): מערך של מספרים.
    
    מחזירה:
    np.array: מערך מנורמל. אם כל הערכים במערך זהים, יש להחזיר מערך של אפסים.
    """
    # המרת הקלט ל-numpy array לצורך חישובים וקטוריים
    data = np.array(data)
    
    import numpy as np

def normalize_array(arr):
    # חישוב ערכי המינימום והמקסימום של המערך
    min_val = np.min(arr)
    max_val = np.max(arr)
    
    # בדיקה האם כל הערכים שווים (כדי למנוע חלוקה באפס)
    if max_val == min_val:
        return np.zeros_like(arr)
    
    # חישוב הנרמול לפי הנוסחה בצורה וקטורית
    # x_norm = (x - min) / (max - min)
    normalized = (arr - min_val) / (max_val - min_val)
    
    return normalized
    pass
    # חשוב לזכור להחליף את pass ב- return

if __name__ == "__main__":
    # כאן הסטודנטים יכולים להריץ בדיקה עצמית מהירה
    test_data = [10, 20, 30, 40, 50]
    print(f"Original: {test_data}")
    print(f"Normalized: {normalized_array(test_data)}")
