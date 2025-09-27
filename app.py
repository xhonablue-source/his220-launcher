"""
HIS220 Michigan History - CognitiveCloud.ai Launcher
Wayne County Community College District • Xavier Honablue, M.Ed.
"""

import streamlit as st

def main():
    st.set_page_config(
        page_title="HIS220 - Michigan History",
        page_icon="🏛️",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .stApp {
        background: #f8f9fa;
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        text-align: center;
        padding: 2rem 0 2rem 0;
        background: white;
        margin-bottom: 2rem;
        border-bottom: 3px solid #2563eb;
    }
    
    .course-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1a202c;
        margin-bottom: 0.3rem;
    }
    
    .college-info {
        font-size: 1rem;
        color: #718096;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    
    .instructor-info {
        font-size: 0.9rem;
        color: #4a5568;
        margin-bottom: 1rem;
    }
    
    .course-details {
        display: flex;
        justify-content: center;
        gap: 2rem;
        flex-wrap: wrap;
        margin-top: 1rem;
    }
    
    .detail-badge {
        font-size: 0.8rem;
        color: #2563eb;
        font-weight: 600;
        background: #dbeafe;
        padding: 0.4rem 0.8rem;
        border-radius: 16px;
        border: 1px solid #bfdbfe;
    }
    
    .progress-summary {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        border-left: 4px solid #2563eb;
    }
    
    .progress-stats {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        gap: 1rem;
        text-align: center;
    }
    
    .stat-number {
        font-size: 1.5rem;
        font-weight: 700;
        color: #2563eb;
    }
    
    .stat-label {
        font-size: 0.8rem;
        color: #4a5568;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* Orange/Yellow Gradient - Used for Course Welcome */
    .featured-section {
        margin: 2rem 1rem;
        background: linear-gradient(135deg, #FF6B35 0%, #F7931E 100%);
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
        color: white;
        text-align: center;
    }

    /* Purple Gradient - Used for Mandatory Week 2 Quiz */
    .special-section {
        margin: 2rem 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
        color: white;
        text-align: center;
    }

    .special-title {
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }

    .special-subtitle {
        font-size: 1rem;
        opacity: 0.9;
        margin-bottom: 1.5rem;
        font-weight: 400;
    }

    .special-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 12px;
        padding: 1.5rem;
        max-width: 600px;
        margin: 0 auto;
        transition: all 0.3s ease;
        cursor: pointer;
        text-decoration: none;
        color: white;
        display: block;
    }

    .special-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
        background: rgba(255, 255, 255, 0.2);
        text-decoration: none;
        color: white;
    }

    .special-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }

    .special-card-title {
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    .special-card-desc {
        font-size: 0.9rem;
        opacity: 0.9;
        line-height: 1.4;
    }
    
    .week-section {
        margin: 1.5rem 1rem;
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        border-left: 4px solid #2563eb;
    }
    
    .week-title {
        font-size: 1rem;
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
    }
    
    .week-number {
        background: #2563eb;
        color: white;
        border-radius: 50%;
        width: 24px;
        height: 24px;
        font-size: 0.8rem;
        font-weight: 600;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 0.8rem;
        flex-shrink: 0;
    }
    
    .lesson-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1rem;
        margin-bottom: 1rem;
    }
    
    .lesson-card {
        background: #f7fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 1rem;
        text-decoration: none;
        color: inherit;
        transition: all 0.2s ease;
        cursor: pointer;
        display: block;
    }
    
    .lesson-card:hover {
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        transform: translateY(-2px);
        text-decoration: none;
        color: inherit;
    }
    
    .lesson-card.active {
        border-color: #68d391;
        background: linear-gradient(135deg, #f0fff4 0%, #f7fafc 100%);
    }
    
    .lesson-card.coming-soon {
        opacity: 0.6;
        cursor: not-allowed;
    }
    
    .lesson-icon {
        font-size: 1.5rem;
        margin-bottom: 0.5rem;
        text-align: center;
    }
    
    .active .lesson-icon {
        color: #38a169;
    }
    
    .coming-soon .lesson-icon {
        color: #a0aec0;
    }
    
    .lesson-title {
        font-size: 0.85rem;
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 0.3rem;
        text-align: center;
        line-height: 1.2;
    }
    
    .lesson-type {
        font-size: 0.7rem;
        color: #718096;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    .assignment-info {
        background: #edf2f7;
        border-radius: 6px;
        padding: 0.8rem;
        margin-top: 1rem;
        border-left: 3px solid #4299e1;
    }
    
    .assignment-title {
        font-size: 0.8rem;
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 0.3rem;
    }
    
    .assignment-desc {
        font-size: 0.75rem;
        color: #4a5568;
        line-height: 1.3;
    }
    
    @media (max-width: 768px) {
        .lesson-grid {
            grid-template-columns: 1fr;
        }
        
        .course-details {
            flex-direction: column;
            align-items: center;
        }
        
        .course-title {
            font-size: 1.5rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # Course Header
    st.markdown("""
    <div class="main-header">
        <h1 class="course-title">🏛️ HIS220: Michigan History</h1>
        <p class="college-info">Wayne County Community College District • CognitiveCloud.ai Launcher</p>
        <p class="instructor-info">Instructor: Xavier Honablue, M.Ed. | Room 204 | honablue@umich.edu</p>
        <div class="course-details">
            <div class="detail-badge">3 Credit Hours</div>
            <div class="detail-badge">45 Contact Hours</div>
            <div class="detail-badge">16 Weeks</div>
            <div class="detail-badge">Mon/Wed 2:00 PM-3:44 PM</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Progress Summary
    st.markdown("""
    <div class="progress-summary">
        <div class="progress-stats">
            <div>
                <div class="stat-number">3</div>
                <div class="stat-label">Active Lessons</div>
            </div>
            <div>
                <div class="stat-number">29</div>
                <div class="stat-label">Coming Soon</div>
            </div>
            <div>
                <div class="stat-number">13</div>
                <div class="stat-label">Assignments</div>
            </div>
            <div>
                <div class="stat-number">100</div>
                <div class="stat-label">Practice Questions</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # UPDATED: Course Welcome (Orange Gradient) - "Portal" deleted from heading
    st.markdown("""
    <div class="featured-section">
        <div class="special-title">🌟 HIS220 Course Welcome 🌟</div>
        <div class="special-subtitle">Your gateway to all course materials and interactive learning tools.</div>
        <a href="https://his-220-michigan.streamlit.app/" target="_blank" class="special-card">
            <div class="special-icon">🏛️📚</div>
            <div class="special-card-title">Launch Your Michigan History Journey</div>
            <div class="special-card-desc">
                Click here for the main course portal, containing interactive lectures, full syllabi,
                study guides, and additional historical resources for HIS220.
            </div>
        </a>
    </div>
    """, unsafe_allow_html=True)

    # Week 2 Quiz (Purple Gradient) - Mandatory Assessment
    st.markdown("""
    <div class="special-section">
        <div class="special-title">📝 Mandatory Weekly Assessment: Updated Week 2 Quiz</div>
        <div class="special-subtitle">100-Question Formative Quiz (100 Points)</div>
        <a href="https://his220-week2.streamlit.app/" target="_blank" class="special-card">
            <div class="special-icon">💯✅</div>
            <div class="special-card-title">Access Updated Week 2 Quiz (100 Points)</div>
            <div class="special-card-desc">
                This is the required 100-point quiz for Week 2, featuring the new instant feedback system. 
                Receive a **green** check for correct answers or a **red** 'X' plus the full contextual explanation immediately after submission.
            </div>
        </a>
    </div>
    """, unsafe_allow_html=True)


    # Week 1: Course Introduction
    st.markdown("""
    <div class="week-section">
        <div class="week-title">
            <div class="week-number">1</div>
            Week 1: Course Introduction
        </div>
        <div class="lesson-grid">
            <div class="lesson-card coming-soon">
                <div class="lesson-icon">📖</div>
                <h4 class="lesson-title">Introduction to Michigan History</h4>
                <p class="lesson-type">Monday • Course Overview</p>
            </div>
            <div class="lesson-card coming-soon">
                <div class="lesson-icon">🗺️</div>
                <h4 class="lesson-title">Michigan Geography & Early Settlement</h4>
                <p class="lesson-type">Wednesday • Historical Context</p>
            </div>
        </div>
        <div class="assignment-info">
            <div class="assignment-title">Welcome Activity</div>
            <div class="assignment-desc">Full credit for all students - Course introduction and expectations</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Week 2: Michigan's First Residents - ACTIVE (Updated CTA link)
    st.markdown("""
    <div class="week-section">
        <div class="week-title">
            <div class="week-number">2</div>
            Week 2: Michigan's First Residents
        </div>
        <div class="lesson-grid">
            <a href="https://his220-week2.streamlit.app/" target="_blank" class="lesson-card active">
                <div class="lesson-icon">🏕️</div>
                <h4 class="lesson-title">Indigenous Peoples of Michigan</h4>
                <p class="lesson-type">Monday • Native American History</p>
            </a>
            <a href="https://his220-week2.streamlit.app/" target="_blank" class="lesson-card active">
                <div class="lesson-icon">🔬</div>
                <h4 class="lesson-title">Archaeological Evidence & Migration</h4>
                <p class="lesson-type">Wednesday • Early Human Settlement</p>
            </a>
        </div>
        <div class="assignment-info">
            <div class="assignment-title">Assignment 1: Indigenous Peoples Reflection (4.6%)</div>
            <div class="assignment-desc">300-400 word reflection on Michigan's Native American history - Due Wednesday</div>
        </div>
        <div class="assignment-info" style="background: #f0fff4; border-left: 3px solid #38a169;">
            <a href="https://his220-week2.streamlit.app/" target="_blank" style="text-decoration: none; display: block;">
                <div style="background: #38a169; color: white; padding: 0.8rem 1.2rem; border-radius: 8px; text-align: center; transition: all 0.2s ease; cursor: pointer;" onmouseover="this.style.background='#2f855a'" onmouseout="this.style.background='#38a169'">
                    <div style="font-weight: 600; margin-bottom: 0.2rem;">📝 ACCESS: Updated Week 2 Quiz (100 Points)</div>
                    <div style="font-size: 0.85rem; opacity: 0.9;">Required formative assessment with immediate red/green explanations.</div>
                </div>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Remaining weeks
    weeks_data = [
        {
            "week": 3, "title": "French Exploration & Colonial Period",
            "lessons": [("French Explorers & Missionaries", "⛵", "Monday"), ("French Colonial Administration", "🏰", "Wednesday")],
            "assignment": "Assignment 2: Colonial Period Analysis (4.6%)"
        },
        {
            "week": 4, "title": "British Colonial Period",
            "lessons": [("British Control & Treaty of Paris", "🇬🇧", "Monday"), ("Pontiac's Rebellion", "⚔️", "Wednesday")],
            "assignment": "Assignment 3: British Colonial Policy Essay (4.6%)"
        },
        {
            "week": 5, "title": "American Revolution Impact",
            "lessons": [("Revolutionary War in Michigan", "🇺🇸", "Monday"), ("Post-Revolutionary Transition", "📜", "Wednesday")],
            "assignment": "Assignment 4: Revolutionary Period Timeline (4.6%)"
        },
        {
            "week": 6, "title": "Northwest Territory",
            "lessons": [("Northwest Ordinance", "📋", "Monday"), ("Territorial Government", "🏛️", "Wednesday")],
            "assignment": "Assignment 5: Territorial Development Paper (4.6%)"
        },
        {
            "week": 7, "title": "War of 1812",
            "lessons": [("War of 1812 in Michigan", "⚔️", "Monday"), ("Fort Mackinac & Detroit Siege", "🏰", "Wednesday")],
            "assignment": "Assignment 6: War of 1812 Impact Analysis (4.6%)"
        },
        {
            "week": 8, "title": "Midterm Examination",
            "lessons": [("Midterm Review", "📚", "Monday"), ("MIDTERM EXAM", "📝", "Wednesday")],
            "assignment": "Midterm Examination (20%)",
            "exam": True
        },
        {
            "week": 9, "title": "Path to Statehood",
            "lessons": [("Territorial Growth", "📈", "Monday"), ("Statehood Achieved (1837)", "🎉", "Wednesday")],
            "assignment": "Assignment 7: Statehood Document Analysis (4.6%)"
        },
        {
            "week": 10, "title": "Economic Development",
            "lessons": [("Lumber Industry Boom", "🌲", "Monday"), ("Mining & Agriculture", "⛏️", "Wednesday")],
            "assignment": "Assignment 8: Economic History Report (4.6%)"
        },
        {
            "week": 11, "title": "Immigration & Growth",
            "lessons": [("Immigration Waves", "🚢", "Monday"), ("Cultural Diversity", "🌍", "Wednesday")],
            "assignment": "Assignment 9: Immigration Patterns Study (4.6%)"
        },
        {
            "week": 12, "title": "Civil War Era",
            "lessons": [("Michigan in the Civil War", "⚔️", "Monday"), ("Thanksgiving Break", "🦃", "Wednesday")],
            "assignment": "Assignment 10: Civil War Contribution Essay (4.6%)"
        },
        {
            "week": 13, "title": "Industrial Revolution",
            "lessons": [("Rise of Detroit", "🏭", "Monday"), ("Auto Industry Beginnings", "🚗", "Wednesday")],
            "assignment": "Assignment 11: Industrialization Analysis (4.6%)"
        },
        {
            "week": 14, "title": "20th Century Michigan",
            "lessons": [("Labor Movement", "✊", "Monday"), ("Great Depression & WWII", "📰", "Wednesday")],
            "assignment": "Assignment 12: 20th Century Timeline Project (4.6%)"
        },
        {
            "week": 15, "title": "Modern Michigan",
            "lessons": [("Post-War Development", "🏙️", "Monday"), ("Contemporary Challenges", "📊", "Wednesday")],
            "assignment": "Assignment 13: Modern Michigan Presentation (4.8%)"
        },
        {
            "week": 16, "title": "Final Examination",
            "lessons": [("Final Review", "📖", "Monday"), ("FINAL EXAM", "📝", "Wednesday")],
            "assignment": "Final Examination (20%)",
            "exam": True
        }
    ]

    for week_info in weeks_data:
        # Only show weeks 3-16 in this loop
        if week_info['week'] >= 3:
            section_class = "week-section"
            
            # Additional style for exams
            assignment_bg = "#edf2f7"
            assignment_border = "#4299e1"
            assignment_desc = 'Weekly historical writing and analysis assignment'
            
            if week_info.get("exam"):
                assignment_bg = "#fff5f5"
                assignment_border = "#e53e3e"
                assignment_desc = 'Comprehensive examination covering course materials'

            st.markdown(f"""
            <div class="{section_class}">
                <div class="week-title">
                    <div class="week-number">{week_info['week']}</div>
                    Week {week_info['week']}: {week_info['title']}
                </div>
                <div class="lesson-grid">
            """, unsafe_allow_html=True)
            
            for lesson_title, icon, day in week_info["lessons"]:
                card_class = "lesson-card coming-soon"
                st.markdown(f"""
                    <div class="{card_class}">
                        <div class="lesson-icon">{icon}</div>
                        <h4 class="lesson-title">{lesson_title}</h4>
                        <p class="lesson-type">{day}</p>
                    </div>
                """, unsafe_allow_html=True)
            
            st.markdown(f"""
                </div>
                <div class="assignment-info" style="background: {assignment_bg}; border-left: 3px solid {assignment_border};">
                    <div class="assignment-title">{week_info['assignment']}</div>
                    <div class="assignment-desc">{assignment_desc}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
