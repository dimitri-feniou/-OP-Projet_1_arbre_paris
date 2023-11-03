import streamlit as st
import reveal_slides as rs

sample_presentation = r"""
<!doctype html>
<html lang="fr">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

		<title>reveal.js</title>

		<link rel="stylesheet" href="dist/reset.css">
		<link rel="stylesheet" href="dist/reveal.css">
		<link rel="stylesheet" href="dist/theme/dracula.css">

		<!-- Theme used for syntax highlighted code -->
		<link rel="stylesheet" href="plugin/highlight/monokai.css">
	</head>
	<body>
		<div class="reveal">
			<div class="slides">
				<section>
					<h3><b>Projet 2 Openclassrooms</b> Analyse des arbres de Paris </h3>
					<div class="r-stack">
						<img src="https://www.notre-planete.info/actualites/images/infrastructures/arbres-Paris.jpg" width="800" height="400">
				</section>
				<section>
					<section style="text-align: left;">
						<h3>Présentation du Projet</h3>
						<ul>
							<b><li>Contexte :</li></b>
							 Participation à un Challenge: dans le cadre du programme<b>"Végétalisons la ville"</b></p>
						</ul>
						<ul>
							<b><li>Objectif:</li></b>
							<p>Réalisez une analyse exploratoire sur le jeu de données sur les arbres de la ville de Paris</p>
						</ul>
					</section>
					<section>
						<h3>Présentation du Projet</h3>
						<ul>
							<b><li>Règle du challenge :</li></b>
									<p>Installer un environnement virtuel dédié pour ce challenge</p>
									<p>Les données doivent être exploitées avec python</p>
						
							<b><li>Livrable attendu :</li></b>
									<p>Support de présentation de notre analyse</p>
									<p>Jupyter notebook de l'analyse</p>	
						</ul>
						</section>
						<section>
							<h3>Environnement virtuel et choix des libraries</h3>
							<h5 style="text-align: left;"><b>1.Environnement virtuel</b></h5>
							<p style="text-align: left;">- Création d'un environnement virtual en local sous ubuntu via Annaconda Nommé <i>Projet_data_arbre</i></br>- Version python du projet : <b>python 3.11.4</b></p>
							<h5 style="text-align: left;"><b>2.Librairies utilisées :</b></h5>
								<li style="text-align: left;">Pandas</li>
								<li style="text-align: left;">Seaborn</li>
								<li style="text-align: left;">Folium</li>
						</section>
				</section>
		<section>
			<section style="text-align: left;">
				<h3>Présentation des données</h3>
					<ul>
						<li>Jeu de données en Open data disponible sur le <a href="https://opendata.paris.fr/explore/dataset/les-arbres/information/?disjunctive.typeemplacement&disjunctive.arrondissement&disjunctive.libellefrancais&disjunctive.genre&disjunctive.espece&disjunctive.varieteoucultivar&disjunctive.stadedeveloppement&disjunctive.remarquable&sort=hauteurenm&refine.remarquable=OUI&dataChart=eyJxdWVyaWVzIjpbeyJjb25maWciOnsiZGF0YXNldCI6Imxlcy1hcmJyZXMiLCJvcHRpb25zIjp7ImRpc2p1bmN0aXZlLnR5cGVlbXBsYWNlbWVudCI6dHJ1ZSwiZGlzanVuY3RpdmUuYXJyb25kaXNzZW1lbnQiOnRydWUsImRpc2p1bmN0aXZlLmxpYmVsbGVmcmFuY2FpcyI6dHJ1ZSwiZGlzanVuY3RpdmUuZ2VucmUiOnRydWUsImRpc2p1bmN0aXZlLmVzcGVjZSI6dHJ1ZSwiZGlzanVuY3RpdmUudmFyaWV0ZW91Y3VsdGl2YXIiOnRydWUsImRpc2p1bmN0aXZlLnN0YWRlZGV2ZWxvcHBlbWVudCI6dHJ1ZSwiZGlzanVuY3RpdmUucmVtYXJxdWFibGUiOnRydWUsInNvcnQiOiItaWRiYXNlIiwicmVmaW5lLnJlbWFycXVhYmxlIjoiT1VJIn19LCJjaGFydHMiOlt7ImFsaWduTW9udGgiOnRydWUsInR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiQVZHIiwieUF4aXMiOiJpZGJhc2UiLCJzY2llbnRpZmljRGlzcGxheSI6dHJ1ZSwiY29sb3IiOiIjMDAzMzY2In1dLCJ4QXhpcyI6InR5cGVlbXBsYWNlbWVudCIsIm1heHBvaW50cyI6NTAsInNvcnQiOiIifV0sInRpbWVzY2FsZSI6IiIsImRpc3BsYXlMZWdlbmQiOnRydWUsImFsaWduTW9udGgiOnRydWV9&basemap=jawg.dark&location=12,48.85652,2.34892">site opendata paris.</a>Données regroupant les arbres gérées par la ville de paris.</li>
						<li>Données disponible dans différents format via l'api ou téléchargement direct</li></ul>
				
			</section>
			<section style="text-align: left;">
				<h3>Contenu du Dataset</h3>
				<ul>
					<li>Notre dataset contient les données de <b>207641</b> arbres de Paris</li>
				</ul>
					<h5><b>Informations disponibles sur les arbres :</b></h5>
				<ul>
					<li>ID</li>
					<li>Adresse</li>
					<li>Géolocalisation</li>
					<li>Espèces</li>
					<li>Arbre Remarquable</li>
					<li>Hauteur/circonférence</li>
					<li>Stade de développement</li>
				</ul>
			</section>
		</section>
	<section>
		<section>
			<h3>Nettoyage des données : Suppression des colonnes inutiles</h3>
				<img style="float: left"width="30%" data-src="./img_presentation/arbres_nul_values.png">
				<ul style="width: 60%;align-content: center;">
					<li> Les colonnes <b>typeemplacement</b>,<b>numero</b><br>,<b>complementadresse</b> sont à supprimer</li>
				</ul>
		</section>
		<section>
			<h3>Nettoyage des données : Suppression des valeurs abbérentes</h3>
			<h5 style="text-align: left;"><b>Le z-score</b></h5>
			<img src="https://dr282zn36sxxg.cloudfront.net/datastreams/f-d%3Ad2cf10f8fe63674ed49bce58cb0a5ebb5ca6a2c314275d310321affd%2BIMAGE_THUMB_POSTCARD_TINY%2BIMAGE_THUMB_POSTCARD_TINY.1" >

		</section>
		<section>
			<h3>Nettoyage des données : Suppression des valeurs abbérentes</h3>
			<h5 style="text-align: left;"><b>Calcul du z-score sur notre jeu de données</b></h5>
			<ul>
				<li> Z-score en fonction de la <b>hauteur</b> et la <b>Circoncéférence</b> des arbres</li>
				<li> Dataset contenant 2356 outliers</li>
			</ul>

		</section>
	</section>
	<section>
	<section>
		<h3>Analyse de données Graphique:Représentation des Arbres dans paris</h3>
		<img src="./img_presentation/arbre_espece.png" style="float: left"width="50%">
		<ul style="width: 40%;">
			<li><b>197 espèces</b> d'arbre différentes à paris</li>
			<li>Diversification des espèces :<br>
				enjeux et climatique et de la survie des arbres </li>
	
		</ul>

	</section>
	<section>
		<h4>Analyse de données Graphique:Représentation des Arbres dans paris</h4>
		<img src="./img_presentation/arbre_espece.png" style="width:80%">
	</section>
</section>	
	<section>
		<h4>Analyse Cartographique:Représentation des arbres par arrondissement</h4>
		<iframe
  id="inlineFrameExample"
  title="Inline Frame Example"
  width="800"
  height="500"
  src="./img_presentation/output.html">
</iframe>
	  </section>
	  <section>
	  <section>
		<h2>Conclusion de l'analyse</h2>

	  </section>
	  <section>
		<h3>Conclusion </h3>
		<h5 style="text-align: left;"><b>Optimisation des tournées</b></h5>
		<ul>
			<li> Favoriser les zones où il y'a des arbres adultes et remarquable</li>
			<li> Favoriser le sud ouest et nord de paris où il y'a une forte concentration d'arbres</li>
			<img src="./img_presentation/arbre_remarquable.png" style="width:40%">
		</ul>


	</section>
	<section>
		<h3>Conclusion </h3>
		<h5 style="text-align: left;"><b>Végétalisation de Paris</b></h5>
		<ul>
			<li>Selon le green view index (MIT) la <b>couverture végétale de paris est de 8,8%</b></li>
			<li>Plan arbre : Objectif <b>170 000 plantations</b> </li>
			<li> <b>Changement climatique</b>: Adapté les essences au risque d’épisodes caniculaires (micocouliers de Provence, les noisetiers de Byzance) </li>
		</ul>

	</section>
</section>		

			</div>
		</div>

		<script src="dist/reveal.js"></script>
		<script src="plugin/notes/notes.js"></script>
		<script src="plugin/markdown/markdown.js"></script>
		<script src="plugin/highlight/highlight.js"></script>
		<script src="plugin/zoom/zoom.js"></script>
		<script>
			// More info about initialization & config:
			// - https://revealjs.com/initialization/
			// - https://revealjs.com/config/
			Reveal.initialize({
				hash: true,
				slideNumber: 'c/t',

				// Learn about plugins: https://revealjs.com/plugins/
				plugins: [ RevealMarkdown, RevealHighlight, RevealNotes,RevealZoom ]
			});
		</script>
	</body>
</html>
"""
st.header("Présentation Projet 2 Analyse Arbre Paris", divider='red')
st.link_button("Lien Projet Github",
               "https://github.com/dimitri-feniou/-OP-Projet_1_arbre_paris")

with st.sidebar:
    st.header("Component Parameters")
    theme = st.selectbox("Theme", ["black", "black-contrast", "blood", "dracula", "moon", "white",
                         "white-contrast", "league", "beige", "sky", "night", "serif", "simple", "solarized"])
    height = st.number_input("Height", value=500)
    st.subheader("Slide Configuration")
    content_height = st.number_input("Content Height", value=900)
    content_width = st.number_input("Content Width", value=900)
    scale_range = st.slider("Scale Range", min_value=0.0,
                            max_value=5.0, value=[0.1, 3.0], step=0.1)
    margin = st.slider("Margin", min_value=0.0,
                       max_value=0.8, value=0.1, step=0.05)
    plugins = st.multiselect("Plugins", [
                             "highlight", "katex", "mathjax2", "mathjax3", "notes", "search", "zoom"], [])
    st.subheader("Initial State")
    hslidePos = st.number_input("Horizontal Slide Position", value=0)
    vslidePos = st.number_input("Vertical Slide Position", value=0)
    fragPos = st.number_input("Fragment Position", value=-1)
    overview = st.checkbox("Show Overview", value=False)
    paused = st.checkbox("Pause", value=False)

# Add the streamlit-reveal-slide component to the Streamlit app.
currState = rs.slides(sample_presentation,
                      height=height,
                      theme="dracula",
                      allow_unsafe_html=True,
                      config={
                          "width": content_width,
                          "height": content_height,
                          "minScale": scale_range[0],
                          "center": True,
                          "maxScale": scale_range[1],
                          "margin": margin,
                          "plugins": plugins
                      },
                      initial_state={
                          "indexh": hslidePos,
                          "indexv": vslidePos,
                          "indexf": fragPos,
                          "paused": paused,
                          "overview": overview
                      },
                      markdown_props={"data-separator-vertical": "^--$"},
                      key="foo")
st.subheader('', divider='red')
st.link_button("Télécharger le code du projet(.zip)",
               "https://github.com/dimitri-feniou/-OP-Projet_1_arbre_paris/raw/main/Projet_2_Feniou_Dimitri.zip")
st.link_button("Télécharger la présentation en PDF (.pdf)",
               "https://raw.githubusercontent.com/dimitri-feniou/-OP-Projet_1_arbre_paris/main/reveal.js-presentation/presentation_arbre.pdf")
