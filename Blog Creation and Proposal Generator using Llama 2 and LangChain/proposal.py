import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function to get response from LLama 2 model
def getLLamaresponse(job_description):
    ### LLama2 model
    llm = CTransformers(
        model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
        model_type='llama',
        config={'max_new_tokens': 256, 'temperature': 0.01}
    )
    
    ## Prompt Template
    template = """
    Generate a job proposal for the above job description give as a proposal letter to submit to the above described work:

    {job_description}
    """
    
    prompt = PromptTemplate(input_variables=["job_description"], template=template)
    
    ## Generate the response from the LLama 2 model
    response = llm(prompt.format(job_description=job_description))
    print(response)
    return response

# Streamlit app setup
st.set_page_config(page_title="Generate Job Proposal", page_icon='🤖', layout='centered', initial_sidebar_state='collapsed')

st.header("Generate Job Proposal 🤖")

# Text area to input job description
job_description = st.text_area("Enter the Job Description")

submit = st.button("Generate Proposal")

## Final response
if submit:
    if job_description:
        proposal = getLLamaresponse(job_description)
        st.write(proposal)
    else:
        st.error("Please enter a job description.")
