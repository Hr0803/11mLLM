import streamlit as st
from page_builder import page_builder
def local_css(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():
    st.title('LLM을 여행하는 프롬프트 엔지니어를 위한 안내서')
    st.write('English-Korean 용어집')
    builder = page_builder()
    menu = builder.menu   
    local_css("style.css")
    # tag_colors = builder.tag_colors  
    columns = st.columns(len(menu))

    # Default choice
    choice = st.session_state.get('choice', 'A')

    for i, item in enumerate(menu):
        if columns[i].button(item):
            choice = item
            st.session_state.choice = item

    st.subheader(choice)
    vocab_data = builder.get_vocab_data(choice)



    for term, details in vocab_data.items():
        with st.expander(term):
            # Targets and Tags
            tag_html = ""
            for tag in details['Tag']:
                tag_class = tag.replace(" ", "-")
                tag_html += f'<div class="tag-container tag-{tag_class}" style="margin-left: 5px;">{tag}</div>'   
            st.markdown(f'''
                <div style="display: flex; align-items: center; justify-content: space-between;">
                    <span>{details['Target']}</span>
                    <div style="display: flex; align-items: center;">{tag_html}</div>
                </div>
            ''', unsafe_allow_html=True)
            
            # Examples and URLs
            try:
                st.markdown("---")
                st.write("**Example:**")
                for example, url in zip(details['Example'], details['URL']):
                    st.markdown(f'''
                    <div class="example-text">
                        {example}
                        <a class="example-link" href="{url}" target="_blank">[⇀ Go to Page]</a>
                    </div>''', unsafe_allow_html=True)
            except:
                None
            st.markdown("&nbsp;")

if __name__ == '__main__':
    main()

