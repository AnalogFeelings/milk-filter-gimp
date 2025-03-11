# :milk_glass: Milk Filter

[![Original](https://img.shields.io/badge/Original_Code-by_LucaSinUnaS-blue?style=flat-square&logo=github)](https://github.com/LucaSinUnaS/Milk-Filter)
[![GitHub issues](https://img.shields.io/github/issues/analogfeelings/milk-filter-gimp?style=flat-square&logo=github&label=Issues)](https://github.com/AnalogFeelings/milk-filter-gimp/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/analogfeelings/milk-filter-gimp?label=Pull%20Requests&style=flat-square&logo=github)](https://github.com/AnalogFeelings/milk-filter-gimp/pulls)
[![GitHub](https://img.shields.io/github/license/analogfeelings/milk-filter-gimp?label=License&style=flat-square&logo=opensourceinitiative&logoColor=white)](https://github.com/AnalogFeelings/milk-filter-gimp/blob/master/LICENSE)
[![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/m/analogfeelings/milk-filter-gimp/main?label=Commit%20Activity&style=flat-square&logo=github)](https://github.com/AnalogFeelings/milk-filter-gimp/graphs/commit-activity)
[![GitHub Repo stars](https://img.shields.io/github/stars/analogfeelings/milk-filter-gimp?label=Stargazers&style=flat-square&logo=github)](https://github.com/AnalogFeelings/milk-filter-gimp/stargazers)
[![Mastodon Follow](https://img.shields.io/mastodon/follow/109309123442839534?domain=https%3A%2F%2Ftech.lgbt%2F&style=flat-square&logo=mastodon&logoColor=white&label=Follow%20Me!&color=6364ff)](https://tech.lgbt/@analog_feelings)

Choose an image you like and turn it into something you'd see in the Milk inside/outside series!  
This was a pain to write, as there was barely any documentation on GIMP's plugin interface and my IDE did not like the GIMP module file much.

> [!IMPORTANT]
> This plugin does not support GIMP 3, support for it may be added in the future.

## :eye: Showcase
![GIMP showcase](screenshots/gimp.gif)

## :package: Installation
Download [milk_filter.py](milk_filter.py) and place it in either of these directories:

- `C:\Program Files\GIMP 2\lib\gimp\2.0\plug-ins`
- `C:\Users\YourUsername\AppData\Roaming\GIMP\2.10\plug-ins`

And reboot GIMP. You should see the filter now appear under **Filters** -> **Artistic** -> **Milk Filter**.

## :warning: Limitations

- This plugin doesn't support changing the color palette, or the brightness thresholds.
- This plugin doesn't support JPEG compression like the original milk filter does, use a pre-compressed image.

# :balance_scale: License

Licensed under the [MIT license](LICENSE), a permissive license.

> [!WARNING]
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.
