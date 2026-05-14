// Product
interface IButton
{
    void Render();
}

// Concrete Products
class WindowsButton : IButton
{
    public void Render() => Console.WriteLine("Windows button");
}

class WebButton : IButton
{
    public void Render() => Console.WriteLine("Web button");
}

// Creator
abstract class Dialog
{
    public abstract IButton CreateButton();

    public void RenderWindow()
    {
        IButton button = CreateButton();
        button.Render();
    }
}

// Concrete Creators
class WindowsDialog : Dialog
{
    public override IButton CreateButton()
        => new WindowsButton();
}

class WebDialog : Dialog
{
    public override IButton CreateButton()
        => new WebButton();
}
