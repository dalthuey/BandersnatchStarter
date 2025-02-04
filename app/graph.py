from altair import Chart, Tooltip
from pandas import DataFrame
import altair as alt

def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    """
    Generates an Altair scatter plot styled to match the Bandersnatch dark theme.

    Parameters:
        df (DataFrame): The dataset containing monster data.
        x (str): Column name for X-axis.
        y (str): Column name for Y-axis.
        target (str): Column name for color encoding.

    Returns:
        Chart: A customized Altair Chart object.
    """
    
    if x not in df.columns or y not in df.columns or target not in df.columns:
        raise ValueError("One or more selected columns do not exist in the dataset.")

    graph = Chart(
        df,
        title=f"{y} by {x} for {target}"
    ).mark_circle(size=40).encode(
        x=x,
        y=y,
        color=alt.Color(target, scale=alt.Scale(scheme='plasma')),
        tooltip=[
            Tooltip('Name', title='Monster Name'),
            Tooltip('Type', title='Category'),
            Tooltip('Level', title='Level'),
            Tooltip('Rarity', title='Rarity Rank'),
            Tooltip('Damage', title='Damage'),
            Tooltip('Health', format='.2f', title='HP'),
            Tooltip('Energy', format='.2f', title='Stamina'),
            Tooltip('Sanity', format='.2f', title='Mind Strength'),
            Tooltip('Timestamp', title='Created At')
        ]
    ).properties(
        width=600,
        height=400,
        background='rgb(34,34,34)',
        padding=15
    ).configure_axis(
        labelColor='lightgray',
        titleColor='white',
        gridColor='gray'
    ).configure_legend(
        labelColor='lightgray',
        titleColor='white'
    ).configure_title(
        fontSize=18,
        fontWeight='bold',
        color='white'
    )

    return graph
