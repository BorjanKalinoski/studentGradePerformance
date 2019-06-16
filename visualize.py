# df['race/ethnicity'].value_counts(normalize=True).plot(kind="bar",alpha=0.5)
# plt.show()
#
# df['gender'].value_counts(normalize=True).plot(kind="bar",alpha=0.5)
# plt.show()
#
# df['parental level of education'].value_counts(normalize=True).plot(kind="bar",alpha=0.5)
# plt.show()
#
# df['lunch'].value_counts(normalize=True).plot(kind="bar",alpha=0.5)
# plt.show()
#
# df['test preparation course'].value_counts(normalize=True).plot(kind="bar",alpha=0.5)
# plt.show()
# leave this commented out
import matplotlib.pyplot as plt
from sop import df


def show_graphs():
    fig = plt.figure(figsize=(18, 6))

    plt.subplot2grid((2, 3), (0, 0))
    df['math score'].value_counts(normalize=True).plot(kind="bar", alpha=0.5)
    plt.title('Math Score')

    plt.subplot2grid((2, 3), (0, 1))
    plt.scatter(df['gender'], df['math score'], alpha=0.2)
    plt.title('Math score wrt gender')

    plt.subplot2grid((2, 3), (0, 2))
    plt.scatter(df['race/ethnicity'], df['math score'], alpha=0.2)
    plt.title('Math score wrt race/ethnicity')

    plt.subplot2grid((2, 3), (1, 0))
    plt.scatter(df['parental level of education'], df['math score'], alpha=0.2)
    plt.title('math score wrt Parental level of education ')

    plt.subplot2grid((2, 3), (1, 1))
    plt.scatter(df['test preparation course'], df['math score'], alpha=0.2)
    plt.title('math score wrt Test preparation course')

    plt.subplot2grid((2, 3), (1, 2))
    plt.scatter(df['lunch'], df['math score'], alpha=0.2)
    plt.title('math score wrt lunch course ')

    plt.show()

    plt.subplot2grid((2, 3), (0, 0))
    df['reading score'].value_counts(normalize=True).plot(kind="bar", alpha=0.5)
    plt.title('Reading Score')

    plt.subplot2grid((2, 3), (0, 1))
    plt.scatter(df['gender'], df['reading score'], alpha=0.2)
    plt.title('Reading score wrt gender')

    plt.subplot2grid((2, 3), (0, 2))
    plt.scatter(df['race/ethnicity'], df['reading score'], alpha=0.2)
    plt.title('reading score wrt race/ethnicity')

    plt.subplot2grid((2, 3), (1, 0))
    plt.scatter(df['parental level of education'], df['reading score'], alpha=0.2)
    plt.title('reading score wrt Parental level of education ')

    plt.subplot2grid((2, 3), (1, 1))
    plt.scatter(df['test preparation course'], df['reading score'], alpha=0.2)
    plt.title('reading score wrt Test preparation course ')

    plt.subplot2grid((2, 3), (1, 2))
    plt.scatter(df['lunch'], df['reading score'], alpha=0.2)
    plt.title('reading score wrt lunch course  ')
    plt.show()
