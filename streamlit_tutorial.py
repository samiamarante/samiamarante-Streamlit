import streamlit as st
# render, heroku, Streamlit Sharing, PythonAnywhere, AWS EC2

def main():
    st.title('Contador Simple')
    
    # Inicializamos el contador en 0
    contador = st.number_input('Contador', value=0)
    
    # Botón para incrementar el contador
    if st.button('Incrementar'):
        contador += 1
    
    # Botón para reiniciar el contador
    if st.button('Reiniciar'):
        contador = 0
    
    # Mostrar el contador actualizado
    st.write('El contador es:', contador)

if __name__ == "__main__":
    main()
# En la línea de comandos ejecutar:
#streamlit run streamlit_tutorial.py 