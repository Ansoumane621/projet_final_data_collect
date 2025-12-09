import pandas as pd
import streamlit as st
import functions.vetement_homme as vetement_homme 
import functions.chaussure_enfant as chaussure_enfant
import functions.chaussures_homme as chaussures_homme
import functions.vetement_enfant as vetement_enfant
import plotly.express as px

# --- Configuration de la page
st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# Utilisation
load_css("styles.css")

# Vérification de la session
if "auth" not in st.session_state:
    st.session_state.auth = False
if "username" not in st.session_state:
    st.session_state.username = ""
    
with st.container():
# --- Contenu principal ---
    if st.session_state.auth:
        st.markdown('<div class="content">',unsafe_allow_html=True)
        st.sidebar.markdown("<p style='font-size:40px,margin-bottom:150px'>User Input Features</p>", unsafe_allow_html=True)

        # Création d'une liste de 1 à 599
        index_list = list(range(1, 600))  # range(n, m) va de n à m-1
        # Premier selectbox avec son propre div
        st.sidebar.markdown('<div id="select_index">', unsafe_allow_html=True)
        add_selectbox = st.sidebar.selectbox('Pages indexes', index_list, key="index_page")
        st.sidebar.markdown('</div>', unsafe_allow_html=True)

        # Deuxième selectbox avec son propre div
        st.sidebar.markdown('<div id="select_option">', unsafe_allow_html=True)
        add_select_file = st.sidebar.selectbox('Options', (
            "Scrape Data beautifulSoup",
            "Download scraped data",
            "Dashbord of the data",
            "Evaluated the App"
        ))
        st.sidebar.markdown('</div>', unsafe_allow_html=True)
        

        st.toast(f"{add_select_file} in the process of selection")

        st.markdown('<div class="app-title">MY BEST DATA APP </div>',unsafe_allow_html=True)
        st.markdown('<div class="app1">This app performs webscraping of data from dakar-auto over multiples pages. And we can also download scraped data from the app directly without scraping them.</div>',unsafe_allow_html=True)
        
        st.markdown('<li class="subtitle">Python libraries: base64, pandas, streamlit, requests, bs4</li>',unsafe_allow_html=True)
        st.markdown('<li class="subtitle">Data source : <a class="link" href="https://www.expat-dakar.com/" target="_blank"> Expat Dakar<a/> <span class="tiret">---</span> <a class="link" href="https://dakar-auto.com/senegal" target="_blank">Dakar Auto<a/></li>',unsafe_allow_html=True)
        
        if add_select_file =='Scrape Data beautifulSoup':
            
            col1, col2, col3 = st.columns([1, 2, 1])  # col2 = au centre
            with col2:
                st.markdown('<div id="button_block">', unsafe_allow_html=True)

                if st.button('Vêtements Hommes'):
                    data = vetement_homme.clear_data(add_selectbox)
                    rows, cols = data.shape
                    st.markdown('<h5>Display data dimension</h5>',unsafe_allow_html=True)
                    st.write(f'<p class="p-t">Data dimension: {rows} rows and {cols} columns.</p>',unsafe_allow_html=True)
                    st.dataframe(data)
                
                    # Convertir en CSV
                    csv = data.to_csv(index=False).encode('utf-8')

                    # Bouton de téléchargement
                    st.download_button(
                        label="Download data as csv",
                        data=csv,
                        file_name="vetement_hommes.csv",
                        mime="text/csv"
                    )

                if st.button('Chaussures Hommes'):
                    data = chaussures_homme.clear_data(add_selectbox)
                    rows, cols = data.shape
                    st.markdown('<h5>Display data dimension</h5>',unsafe_allow_html=True)
                    st.write(f'<p class="p-t">Data dimension: {rows} rows and {cols} columns.</p>',unsafe_allow_html=True)
                    st.dataframe(data)
                    # Convertir en CSV
                    csv = data.to_csv(index=False).encode('utf-8')

                    # Bouton de téléchargement
                    st.download_button(
                        label="Download data as csv",
                        data=csv,
                        file_name="chaussures_hommes.csv",
                        mime="text/csv"
                    )

                if st.button('Vêtements Enfants'):
                    data = vetement_enfant.clear_data(add_selectbox)
                    rows, cols = data.shape
                    st.markdown('<h5>Display data dimension</h5>',unsafe_allow_html=True)
                    st.write(f'<p class="p-t">Data dimension: {rows} rows and {cols} columns.</p>',unsafe_allow_html=True)
                    st.dataframe(data)
                    # Convertir en CSV
                    csv = data.to_csv(index=False).encode('utf-8')

                    # Bouton de téléchargement
                    st.download_button(
                        label="Download data as csv",
                        data=csv,
                        file_name="vetement_enfants.csv",
                        mime="text/csv"
                    )

                if st.button('Chaussures Enfants'):
                    data = chaussure_enfant.clear_data(add_selectbox)
                    rows, cols = data.shape
                    st.markdown('<h5>Display data dimension</h5>',unsafe_allow_html=True)
                    st.write(f'<p class="p-t">Data dimension: {rows} rows and {cols} columns.</p>',unsafe_allow_html=True)
                    st.dataframe(data)
                    # Convertir en CSV
                    csv = data.to_csv(index=False).encode('utf-8')

                    # Bouton de téléchargement
                    st.download_button(
                        label="Download data as csv",
                        data=csv,
                        file_name="chaussure_enfant.csv",
                        mime="text/csv"
                    )

                st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('</div>',unsafe_allow_html=True)
        elif add_select_file == 'Download scraped data':
            col1, col2, col3 = st.columns([1, 2, 1])  # col2 = au centre
            with col2:
                st.markdown('<div id="button_block">', unsafe_allow_html=True)

                if st.button('Vêtements Hommes'):
                    # data = vetement_homme.main_info_vetement(119)
                    data = pd.read_csv('data/vetement_hommes.csv')
                    rows, cols = data.shape
                    st.markdown('<h5>Display data dimension</h5>',unsafe_allow_html=True)
                    st.write(f'<p class="p-t">Data dimension: {rows} rows and {cols} columns.</p>',unsafe_allow_html=True)
                    st.dataframe(data)
                
                    # Convertir en CSV
                    csv = data.to_csv(index=False).encode('utf-8')

                    # Bouton de téléchargement
                    st.download_button(
                        label="Download data as csv",
                        data=csv,
                        file_name="vetement_hommes.csv",
                        mime="text/csv"
                    )

                if st.button('Chaussures Hommes'):
                    # data = chaussures_homme.main_info_chaussures_hommes(119)
                    data = pd.read_csv('data/chaussures_hommes.csv')
                    rows, cols = data.shape
                    st.markdown('<h5>Display data dimension</h5>',unsafe_allow_html=True)
                    st.write(f'<p class="p-t">Data dimension: {rows} rows and {cols} columns.</p>',unsafe_allow_html=True)
                    st.dataframe(data)
                    # Convertir en CSV
                    csv = data.to_csv(index=False).encode('utf-8')

                    # Bouton de téléchargement
                    st.download_button(
                        label="Download data as csv",
                        data=csv,
                        file_name="chaussures_hommes.csv",
                        mime="text/csv"
                    )

                if st.button('Vêtements Enfants'):
                    # data = vetement_enfant.main_info_vetements_enfants(119)
                    data = pd.read_csv('data/vetement_enfants.csv')
                    rows, cols = data.shape
                    st.markdown('<h5>Display data dimension</h5>',unsafe_allow_html=True)
                    st.write(f'<p class="p-t">Data dimension: {rows} rows and {cols} columns.</p>',unsafe_allow_html=True)
                    st.dataframe(data)
                    # Convertir en CSV
                    csv = data.to_csv(index=False).encode('utf-8')

                    # Bouton de téléchargement
                    st.download_button(
                        label="Download data as csv",
                        data=csv,
                        file_name="vetement_enfants.csv",
                        mime="text/csv"
                    )

                if st.button('Chaussures Enfants'):
                    # data = chaussure_enfant.main_info_chaussures_enfants(119)
                    data = pd.read_csv('data/chaussure_enfant.csv')
                    rows, cols = data.shape
                    st.markdown('<h5>Display data dimension</h5>',unsafe_allow_html=True)
                    st.write(f'<p class="p-t">Data dimension: {rows} rows and {cols} columns.</p>',unsafe_allow_html=True)
                    st.dataframe(data)
                    # Convertir en CSV
                    csv = data.to_csv(index=False).encode('utf-8')

                    # Bouton de téléchargement
                    st.download_button(
                        label="Download data as csv",
                        data=csv,
                        file_name="chaussure_enfant.csv",
                        mime="text/csv"
                    )

                st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('</div>',unsafe_allow_html=True)
            
        elif add_select_file == 'Dashbord of the data':
            data = chaussure_enfant.main_info_chaussures_enfants(1)
            col1, = st.columns([1])  # col2 = au centre
            with col1:
                st.markdown('<div id="button_block">', unsafe_allow_html=True)
                import plotly.express as px

                import plotly.express as px

                for col in data.columns:
                    if col == "link_image":
                        continue
                    st.subheader(f"Graphique : {col}")
                    
                    if data[col].dtype in ['int64','float64']:
                        fig = px.histogram(data, x=col)
                        st.plotly_chart(fig, use_container_width=True)

                    else:
                        vc = data[col].value_counts().reset_index()
                        vc.columns = [col, 'count']

                        fig = px.bar(vc, x=col, y='count')
                        st.plotly_chart(fig, use_container_width=True)

                
                st.markdown('</div>',unsafe_allow_html=True)
        elif add_select_file == 'Evaluated the App':
            
            st.markdown('<div id="button_block">', unsafe_allow_html=True)
            row1,row2 = st.columns([1,1])
            with row1:
                # st.button('Kobo Evaluation Form',on_click="")
                st.markdown("""
                    <a href="https://ee.kobotoolbox.org/x/C7t0bE6G" target="_blank">
                        <button class="btn">
                            Kobo Evaluation Form
                        </button>
                    </a>
                """, unsafe_allow_html=True)

                with row2:
                    st.markdown("""
                    <a href="https://docs.google.com/forms/d/e/1FAIpQLSeYQOIjKDaWRFzufFE19ZxTnlZOMM29GHE5-_1cLGYlaIDGxg/viewform?usp=dialog" target="_blank">
                        <button class="btn">
                            Google Evaluation Form
                        </button>
                    </a>
                """, unsafe_allow_html=True)
                    

            st.markdown('</div>',unsafe_allow_html=True)

    else:
        st.toast("Veuillez vous connecter pour accéder à l'application.")
        st.switch_page('./DECONNEXION.py')
    
    